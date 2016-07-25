#!/usr/bin/env python

import datetime as dt
import json
import sys
from apiclient.discovery import build

def getURLs(search_term, num_requests):
    # Key codes we created earlier for the Google CustomSearch API

    #old
    #search_engine_id = '004825588201602563535:cnwl6gumo1w'
    #api_key = 'AIzaSyBnTOe-2s4nbfWi2FotINYHx6yVbiipIV4'

    #new
    search_engine_id = '011895802445678870302:5kryptu5h44'
    api_key = 'AIzaSyBjlqdIm4A95sg8kWDv_ohtrlPlyTFMpao'

    # The build function creates a service object. It takes an API name and API
    # version as arguments. 
    service = build('customsearch', 'v1', developerKey=api_key)
    # A collection is a set of resources. We know this one is called "cse"
    # because the CustomSearch API page tells us cse "Returns the cse Resource".
    collection = service.cse()

    urls = []
    for i in range(0, num_requests):
        # This is the offset from the beginning to start getting the results from
        start_val = 1 + (i * 10)
        # Make an HTTP request object
        request = collection.list(q=search_term,
            num=10, #this is the maximum & default anyway
            start=start_val,
            cx=search_engine_id
        )

        response = request.execute()
        output = json.dumps(response, sort_keys=True, indent=2)

        decoded = json.loads(output)

        for j in range(0,10):
            dlink = decoded['items'][j]['displayLink']
            link = decoded['items'][j]['link']

            if ("www.facebook.com" in link) or ("www.youtube.com" in link) or (".pdf" in link):
                continue
               
            urls.append(decoded['items'][j]['link'])

    return urls

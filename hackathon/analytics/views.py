from django.shortcuts import render
from django.http import HttpResponse
from analytics import ExtractText
from analytics import GetURLs
from analytics.sentiment import *
from analytics.GetTweets import *
from analytics.WikipediaArticleIntro import *
import json

def index(request):
    stats = {'status':'fail'}
    tweets = []
    split_tweets = []
    wiki = ""
    if request.method == "POST":
        query = request.POST['Search']
        stats = get_data_from_url(query)
        tweets = getTweets(query)
        wiki=getWikiText(query)
        for ii in tweets:
            split_tweets.append(ii.split(':', 2))
        print(split_tweets)
    return render(request,
                  'analytics\\home.html',
                  {'extend_template': 'analytics\\template.html',
                   'stats': stats,
                   'tweets': split_tweets,
                   'wiki': wiki,})


"""def get_sentiment_data(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)"""


def get_data_from_url(query_string):
    urls = []

    urls = GetURLs.getURLs(query_string, 2)
    i = 0

    result_stats = []
    for url in urls:
        data = ""

        data = ExtractText.getArticleTextFromURL(url)
        if (data == ""):
            print("Retrying with Paragraph extraction..")
            data = ExtractText.getParaTextFromURL(url)
        if (data == ""):
            print("Could not extract with Para extraction. Skipping URL..")
            continue
        i += 1
        print("Calculating Sentiment")
        s = Sentiment(data)
        sentiment = s.get_positive_negative_for_text()
        result_stats.append(sentiment)

    retVal = {'status': 'success',
                  'result_stats': result_stats}
    return retVal

        #return HttpResponse("Hello, world. You're at the polls index.")
    # Create your views here.

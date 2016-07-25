import subprocess
import json
import sys
import os.path
import hackathon.settings as settings
import re

def getTweets(searchTerm):
    directory = settings.BASE_DIR + "\\analytics\\scripts\\tweets.r"
    cmd = "Rscript " + directory + " " + searchTerm
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    index = output.find(b"Using direct authentication")
    #output = output.replace('[[*%d*]]', ' SK')

    out = output.decode("utf-8", "ignore")

    out = out[index+30:].replace("\r", "")

    tweets = re.findall(r'\".*\"', out)

    tweets = [t.replace('\"', '') for t in tweets]

    return tweets


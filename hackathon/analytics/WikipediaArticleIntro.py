import json
import urllib.request
import urllib.error
import wikipedia

def getWikiText(searchTerm):
	return wikipedia.summary(searchTerm)


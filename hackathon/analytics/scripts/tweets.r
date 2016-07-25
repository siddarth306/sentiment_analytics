#connect all libraries
 library(twitteR)
 library(ROAuth)
 library(plyr)
 library(dplyr)
 library(stringr)
 library(ggplot2)
 require(RCurl)

#connect to API
#download.file(url='http://curl.haxx.se/ca/cacert.pem', destfile='cacert.pem')
reqURL <- 'https://api.twitter.com/oauth/request_token'
accessURL <- 'https://api.twitter.com/oauth/access_token'
authURL <- 'https://api.twitter.com/oauth/authorize'
consumerKey <- 'yJ1LnozygOeFb9pcJVCBkRRru' #put the Consumer Key from Twitter Application
consumerSecret <- 'IQYSszdrJDwNTsdZOOrSRV0VYBTeTwButEZ4eyOUlpB12Op84Z'  #put the Consumer Secret from Twitter Application
ACCESS_TOKEN <- '3300748153-Q26NfOkuJLJwbAMwA5kd2lNkUn0ZmwPsFbt64eS'
ACCESS_SECRET <- 'kl8PYQ04D02e7dno0dGx5Dljq2iO7ueVyqNPTNRIwWdC0'

Cred <- OAuthFactory$new(consumerKey=consumerKey,consumerSecret=consumerSecret,requestURL=reqURL,accessURL=accessURL,authURL=authURL)
#Cred$handshake(cainfo = system.file('CurlSSL', 'cacert.pem', package = 'RCurl')) #There is URL in Console. You need to go to it, get code and enter it on Console

save(Cred, file='twitter authentication.Rdata')
load('twitter authentication.Rdata') #Once you launch the code first time, you can start from this line in the future (libraries should be connected)
setup_twitter_oauth(consumerKey, consumerSecret, ACCESS_TOKEN,ACCESS_SECRET)

args <- commandArgs(trailingOnly = TRUE)
searchTerm <- args[1]
tweets = searchTwitter(searchTerm, n=10 , lang = "en")
print(tweets)

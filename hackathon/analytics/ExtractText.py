from newspaper import Article
import urllib.request
import urllib.error
import sys
from bs4 import BeautifulSoup

def getArticleTextFromURL(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
    except Exception as ex:
        print("Unexpected error!\nError : " + str(ex))
        return ""
    return article.text

def getParaTextFromURL(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    #headers['User-Agent'] = 'Mozilla/5.0'
    try:
        req = urllib.request.Request(url, headers=headers)
        print("Requesting data from " + url)
        resp = urllib.request.urlopen(req, timeout=10)

        respData = resp.read()

    except (ValueError, urllib.error.HTTPError, urllib.error.URLError) as ex:
        print("Error : {0}\n".format(str(ex)))
        return ""
    except Exception as e:
        print("Unexpected error!\nError : " + str(e))
        return ""

    soup = BeautifulSoup(str(respData), "lxml")

    paras = [str(p.get_text()) for p in soup.find_all("p", text=True)]
    webText = " ".join(str(e) for e in paras)
    #webText.decode("utf-8", "ignore")
    return webText

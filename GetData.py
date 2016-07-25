import urllib.request
import urllib.error
import sys
from bs4 import BeautifulSoup

#url = "http://www.gamespot.com/reviews/pokemon-go-review/1900-6416477/"

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
#headers['User-Agent'] = 'Mozilla/5.0'
#keyword = 'Veritas+Netbackup+reviews'
keyword = 'Pokemon+Go'

urls = []
t = "https://www.google.co.in/search?tbm=nws&q="
for start in range(0,5):
	url = "https://www.google.co.in/search?q=" + keyword + "&start=" + str(start*10)
	print(url)
	try:
		req = urllib.request.Request(url, headers=headers)
		resp = urllib.request.urlopen(req, timeout=10)
		respData = resp.read()

		soup = BeautifulSoup(respData, "lxml")
	except (ValueError, urllib.error.HTTPError, urllib.error.URLError) as ex:
		print("Error : {0}\n".format(str(ex)))
		continue
	except:
		print("Unexpected error!")
		continue

	for x in soup.findAll("h3", { "class" : "r" }):
		# removing the html codes from the URL tags
		url_tag = x.find_all('a')[0]
		tempURL = url_tag['href']
		tempURL = tempURL.split("&")[0].split("/url?q=")[-1]
		print(tempURL)

		if '..' in tempURL:
			continue
		else:

			if 'www' not in tempURL and  'http' not in tempURL:
				tempURL = 'www.' + tempURL

			if 'http' not in tempURL:
				tempURL = 'http://' + tempURL

			validURL=tempURL
			print(validURL)
			urls.append(validURL)

i = 0
for url in urls:
	webText = ""
	try:
		req = urllib.request.Request(url, headers=headers)
		print("Requesting data from " + url)
		resp = urllib.request.urlopen(req, timeout=10)

		respData = resp.read()

	except (ValueError, urllib.error.HTTPError, urllib.error.URLError) as ex:
		print("Error : {0}\n".format(str(ex)))
		continue
	except:
		print("Unexpected error!")
		continue

	soup = BeautifulSoup(str(respData), "lxml")

	paras = [str(p.get_text()) for p in soup.find_all("p", text=True)]
	webText = " ".join(str(e) for e in paras)

	print("Data recieved. Writing the data to file...")
	fileName = "Data"+str(i)+".txt"

	try:
		with open(fileName, "w") as dfile:
			dfile.write(str(webText))
	except Exception as ex:
		print("Error : {0}\n".format(str(ex)))

	i += 1
	
	print("Website done: " + str(i))
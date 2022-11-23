# @author: bbaasan
# date: 11/22/2022
# bbaasan@gmu.edu


from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

'''
url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/list"
querystring = {"id":"amzn","until":"0","since":"0","size":"20","number":"1"}
headers = {
	"X-RapidAPI-Key": "da88a4fb89msh9c95d4a78e66fb3p10a314jsn2176d7c3c2b3",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

self = 'https://seekingalpha.com'
#print(response.json()['data'][0]['attributes']['title'])
params = {'p':'class'}
url2 = ''.join((self, response.json()['data'][0]['links']['self']))
resp = requests.get(url2, params=params)

url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
page = requests.get(url)
#print(page.text)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#table = soup.find_all('article', attrs={'class':'bagA mcA cmA cnX cnBK uaB cnL cnCE uaB cnL cnCE uaF uaF bagB'})
table = soup.find_all('a')
#print(table)

#print(soup.find_all('article', attrs={'class':'bagA mcA cmA cnX cnBK uaB cnL cnCE uaB cnL cnCE uaF uaF bagB'}))
'''
"""
url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/get-details"
#querystring = {"id":"4341792"}
querystring = {"id":"aapl","until":"0","since":"0","size":"20","number":"1"}
headers = {
	"X-RapidAPI-Key": "da88a4fb89msh9c95d4a78e66fb3p10a314jsn2176d7c3c2b3",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json()['data']['attributes']['title'])
print(response.json()['data']['attributes']['content'])

"""
url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/list"

querystring = {"id":"amzn","until":"0","since":"0","size":"20","number":"1"}
headers = {
	"X-RapidAPI-Key": "da88a4fb89msh9c95d4a78e66fb3p10a314jsn2176d7c3c2b3",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

self = 'https://seekingalpha.com'
resp = response.json()
for i in range(len(resp['data'])):
    title = resp['data'][i]['attributes']['title']
    other = resp['data'][i]['links']['self']
    url3 = urljoin(self, other)
    my_resp = requests.get(url3, 'html.parser')
    soup = BeautifulSoup(my_resp.content, 'html5lib')
    print('==========This is a line ======================\n\n')
    text = [''.join(s.findAll(text=True)) for s in soup.findAll('p')]
    for item in text:
        print(item)#, file=outfile)

    #print(soup.prettify())
    #lists = soup.findAll('span', attrs={'class':"question"})
    #for i in lists:
    #    print(i)

"""
from collections import Counter
urls = ["http://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart","http://en.wikipedia.org/wiki/Golf"]

with open('thisisanew.txt', 'w', encoding='utf-8') as outfile:
    for url in urls:
        website = requests.get(url)
        soup = BeautifulSoup(website.content, 'html5lib')
        text = [''.join(s.findAll(text=True))for s in soup.findAll('p')]
        for item in text:
            print(item, file=outfile)
"""
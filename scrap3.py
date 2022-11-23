# @author: bbaasan
# date: 11/22/2022
# bbaasan@gmu.edu

from bs4 import BeautifulSoup
import requests
from csv import writer
from requests_html import HTMLSession
import csv
#from selenium import webdriver
from pandas import DataFrame
#driver = webdriver.Chrome()
import os

s = HTMLSession()


def get_transcript_links(page):
    
    links = []
    #url = f'https://seekingalpha.com/earnings/earnings-call-transcripts/'
    r = s.get(page)
    for i in r.html.find('div article'):
        name = i.find('a', first=True).attrs['aria-label']
        href = i.find('a', first=False)[1].attrs['href']
        joined = ''.join(('https://seekingalpha.com', href))
        links.append({
            'names': name,
            'url':joined
        })
    
    return links


def main():
    
    print(os.getcwd())
    os.mkdir('transcripts')
    
    transcripts = []
    
    for i in range(1, 11600, 1):
        print('Getting page: ', i)
        url = f'https://seekingalpha.com/earnings/earnings-call-transcripts?page={i}'
        df = DataFrame(get_transcript_links(url))
        transcripts.append(df)
    
    print(transcripts)
        
if __name__ == '__main__':
    main()
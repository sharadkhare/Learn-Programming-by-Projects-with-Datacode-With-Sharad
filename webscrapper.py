# Web Scraper with Python
# In this article, I’m going to create a web scraper with Python that pulls all the stories from Google News by extracting all the tags from the HTML of Google News.

import urllib.request
from bs4 import BeautifulSoup

class scraper:
    def __init__(self, site):
        self.site = site 
    def scrape(self):
        sharad = urllib.request.urlopen(self.site)
        html = sharad.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)
    
news = "https://news.google.com/"
scraper(news).scrape()   
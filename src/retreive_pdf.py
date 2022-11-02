import numpy as np
import scipy as sci
import tensorflow as tf
import keras as ks
import pandas as pd
import requests
from pathlib import Path
import os
import urllib.request
import sys
from bs4 import BeautifulSoup as bs
import wget

# Check validity of the URL
def check_validity(my_url):
    try:
        urllib.request.urlopen(my_url)
        print("Valid URL")
    except IOError:
        print ("Invalid URL")
        sys.exit()

# Get the PDFs
def get_pdfs(my_url):
    links = []
    html = urllib.request.urlopen(my_url).read()
    html_page = bs(html, features="lxml") 
    og_url = html_page.find("meta",  property = "og:url")
    base = urllib.request.urlparse(my_url)
    print("base",base)
    for link in html_page.find_all('a'):
        current_link = link.get('href')
        if current_link.endswith('pdf'):
            if og_url:
                print("currentLink",current_link)
                links.append(og_url["content"] + current_link)
            else:
                links.append(base.scheme + "://" + base.netloc + current_link)

    for link in links:
        try: 
            wget.download(link)
        except:
            print(" \n \n Unable to Download A File \n")

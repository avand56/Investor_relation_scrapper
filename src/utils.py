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
from bs4 import BeautifulSoup 
import wget


# Check validity of the URL
def check_validity(my_url):
    try:
        urllib.request.urlopen(my_url)
        print("Valid URL")
    except IOError:
        print ("Invalid URL")
        sys.exit()

def get_urls(url,company,target_dir):
    # Requests URL and get response object
    response = requests.get(url)
    
    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all hyperlinks present on webpage
    links = soup.find_all('a')
    
    i = 0
    
    # From all links check for pdf link and
    # if present download file
    for link in links:
        if ('.pdf' in link.get('href', [])):
            i += 1
            print("Downloading file: ", i)
    
            # Get response object for link
            response = requests.get(link.get('href'))
            pdf_name = link.get('href').rsplit('/', 1)[1]
        
            file_path = os.path.join(target_dir, company, pdf_name)
            if os.path.exists(file_path):
                continue
            else:
                dir = os.path.join(target_dir, company)
                os.makedirs(dir, exist_ok=True)
        
                # Write content in pdf file
                pdf = open(file_path, 'wb')
                pdf.write(response.content)
                pdf.close()
                print("File ", i, " downloaded")
    
    print("All PDF files downloaded")

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
from src.utils import(
    check_validity,
    get_urls,
)

class RetreivePDF:
    """ 
    A class to build the pipeline to retreive the PDF files needed
    """
    df = pd.read_excel('/Users/alexvanderhoeff/Desktop/mining_companies.xlsx')
    data_path = df['Paths'].tolist()
    folder = df['Folder'].tolist()
    company = df['Name'].tolist()


    for ind in range(len(0,df)):
        os.makedirs(os.path.join(data_path[ind], company[ind]), exist_ok=False)
        check_validity(data_path[ind])
        get_urls(data_path[ind],company[ind])





# works, it downloads only the pdf files we don't currently have in the directory specified.
my_url = 'https://www.tsx.com/listings/listing-with-us/sector-and-product-profiles/mining'
check_validity(my_url)
get_urls(my_url, 'tsx', '/Users/alexvanderhoeff/Desktop/Documents')

list_of_datasets=pd.read_csv(data)
for val in list_of_datasets[0]:
    check_validity(my_url)
    get_urls(my_url, list_of_datasets[1], '/Users/alexvanderhoeff/Desktop/Documents')

#TODO need to now try and looping through list with company info (company, link) and extracting what we want.
# Once done, we gather all links to investor relations we want and try it on that list.

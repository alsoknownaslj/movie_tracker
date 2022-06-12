# Add new movie to Airtable spreadsheet w/ IMDB link

import pandas as pd
import metadata_parser
import os
import pyairtable
from pyairtable import Table
from pyairtable import formulas as fo
from pyairtable.utils import attachment
import urllib.request
import os

os.getcwd()
os.chdir('/Users/laurenjackson/Desktop/PYTHON/')
os.getcwd()

############################
# Get & clean movie metadata
############################

url = input('Enter IMDB URL')
page = metadata_parser.MetadataParser(url)
blob = page.metadata

print(blob['og'])
movie = {}
movie = blob['og'].copy()
movie.pop('site_name')
movie.pop('type')
movie.pop('image:height')
movie.pop('image:width')
movie.pop('locale')
movie.pop('locale:alternate')

#####################
# Set table variables
#####################

title = movie['title'][:-14]
print(title)

director = movie['description']
start = director.find('Directed by ')
end = director.find('.')
director = director[start+len('Directed by '):end]
print(director)

link = movie['url']
print(link)

image = movie['image']
print(image)

###################################
# Connect table with pyairtable/API
###################################

base_id = 'appl15niec6bWI348'
table_name = 'Watched Films'
api_key = 'key3Ulbqysr6JTWo8'
table = Table(api_key,base_id,table_name)

############################
# Create new record in table
############################

table.create({'TITLE':title,
              'DIRECTOR':director,
              'LINK':link,
             'POSTER': [attachment(image)]})

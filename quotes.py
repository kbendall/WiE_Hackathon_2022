import requests
import json

# import urllib library
from urllib.request import urlopen
import random
import re

# store the URL in url as 
# parameter for urlopen
url = "https://zenquotes.io/api/quotes/"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())

for i in range(50):
    print(data_json[i]['q'])

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

# Open a file with access mode 'a'
file_object = open('sample.txt', 'w')

for x in data_json:
    file_object.write(str(x)+"\n")
# Close the file
file_object.close()


myfile = open("sample.txt", "rt") # open lorem.txt for reading text
contents = myfile.read()         # read the entire file to string
myfile.close()                   # close the file

lines = open('sample.txt').read().splitlines()
myline =random.choice(lines)


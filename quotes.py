import json

# import urllib library
from urllib.request import urlopen


def getQuote():
    # store the URL in url as 
    # parameter for urlopen
    url = "https://zenquotes.io/api/random/"
    
    # store the response of URL
    response = urlopen(url)
    
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    output = data_json[0]['q']
    return(output)

import json
import requests
import urllib.parse
from pprint import pprint 


# r = requests.get('http://www.omdbapi.com/?s=Jaws&apikey=a958712b')

searchString = "Jaws 3"
encodedStr = urllib.parse.quote(searchString, safe='')
# print(encodedStr)
baseURL = 'http://www.omdbapi.com/'
searchStr = '?s=' + encodedStr
apiKey = '&apikey=a958712b'

fullUrl = baseURL + searchStr + apiKey
r = requests.get(fullUrl)

data = json.loads(r.text)

for item in data.items():
    pprint(item)

# # nested dictionary access
# for item in data['Ratings']:
#     pprint(item['Value'])

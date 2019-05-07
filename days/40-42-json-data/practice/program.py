import json
import requests
import urllib.parse
from pprint import pprint 

def main():       
    searchString = input("Enter a movie title to search: ")
    encodedStr = urllib.parse.quote(searchString, safe='')
    # print(encodedStr)
    baseURL = 'http://www.omdbapi.com/'
    searchStr = '?s=' + encodedStr
    apiKey = '&apikey=a958712b'

    fullUrl = baseURL + searchStr + apiKey
    r = requests.get(fullUrl)

    data = json.loads(r.text)

    if(data['Response'] == 'True'):
        print('Movies found:')
        for item in data['Search']:
            print('{} ({})'.format(item['Title'], item['Year']))

    else:
        print(f"Sorry, no movies found containing the title '{searchString}'")

if __name__ == "__main__":
    main()

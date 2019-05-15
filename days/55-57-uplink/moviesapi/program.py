
from api import MovieSearchClient


def main():
    
    val = 'RUN'

    while val:
        print("What would you like to do next?")
        val = input("search by [k]eyword, [d]irector name, or [i]mdb id? ")

        if val == 'k':
            get_movies_by_keyword()
        elif val == 'd':
            get_movies_by_director()
        elif val == 'i':
            get_movies_by_imdb_id()


def get_movies_by_keyword():
    inputKeyword = input("Enter a keyword: ")
    svc = MovieSearchClient()
    response = svc.search_by_keyword(inputKeyword)
    #response.raise_for_status()
    #print(response)

    results = response.json()
    resultHits = results.get('hits')

    for idx, s in enumerate(resultHits, 1):
        print("{}. Title: {}".format(
            idx,
            s.get('title')
        ))


def get_movies_by_director():
    inputKeyword = input("Enter a director name: ")
    svc = MovieSearchClient()
    response = svc.search_by_director(inputKeyword)
    #response.raise_for_status()
    #print(response)

    results = response.json()
    resultHits = results.get('hits')

    for idx, s in enumerate(resultHits, 1):
        print("{}. Title: {}".format(
            idx,
            s.get('title')
        ))


def get_movies_by_imdb_id():
    inputKeyword = input("Enter IMDB ID: ")
    svc = MovieSearchClient()
    response = svc.search_by_imdb_number(inputKeyword)
    #response.raise_for_status()
    #print(response)

    results = response.json()
    print("Title: {}".format(
            results.get('title')
    ))


if __name__ == "__main__":
    main()


import uplink
import requests
import datetime
from uplink_helpers import raise_for_status


@uplink.json
@raise_for_status
class MovieSearchClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def search_by_keyword(self, keyword) -> requests.models.Response:
        """ Gets movies by keyword """
    
    @uplink.get('/api/director/{director_name}')
    def search_by_director(self, director_name) -> requests.models.Response:
        """ Gets movies by director name """
    
    @uplink.get('/api/movie/{imdb_id}')
    def search_by_imdb_number(self, imdb_id) -> requests.models.Response:
        """ Gets movies by imdb id """

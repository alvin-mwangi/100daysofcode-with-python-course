import uplink
import requests
import datetime
from uplink_helpers import raise_for_status


@uplink.json
@raise_for_status
class BlogClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://consumer_services_api.talkpython.fm')

    @uplink.get('/api/blog')
    def all_entries(self) -> requests.models.Response:
        """ Gets all blog entries from the server. """
    
    @uplink.get('/api/blog/{post_id}')
    def entry_by_id(self, post_id) -> requests.models.Response:
        """ Gets single blog post details. """

    def create_new_entry(self, title: str, content: str, 
                         views: int, published: str=None) -> requests.models.Response:
        
        if published is None:
            published = datetime.datetime.now().isoformat()

        return self.__create_new_entry(
            title=title,
            content=content,
            view_count=views,
            published=published
        )


    @uplink.post('/api/blog')
    def __create_new_entry(self, **kwargs: uplink.Body) -> requests.models.Response:
        """ Creates a new post """
    
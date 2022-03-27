import falcon
from utils import Access

class Users:
    @falcon.before(Access.Access(['admin']), is_async=True)
    async def on_get(self, req, resp):
        '''
        Handles GET requests
        '''
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {
            'id': 12332123,
            'eventid': 12,
            'datetime': 1,
            'value': 1
        }
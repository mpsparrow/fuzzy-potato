import falcon
import datetime

class Info:
    async def on_get(self, req, resp):
        '''
        Handles GET requests
        '''
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_JSON
        resp.media = {
            'version': 1,
            'datetime': str(datetime.datetime.now())
        }
'''
Run using unicorn app:app
'''

from types import NoneType
import falcon
import falcon.asgi
import Info
from user import Users
from utils import User

class AuthMiddleware:
    async def process_request(self, req, resp):
        """Process the request before routing it.

        Note:
            Because Falcon routes each request based on req.path, a
            request can be effectively re-routed by setting that
            attribute to a new value from within process_request().

        Args:
            req: Request object that will eventually be
                routed to an on_* responder method.
            resp: Response object that will be routed to
                the on_* responder.
        """
        username = req.get_header('username')
        if username is None:
            raise falcon.HTTPStatus(falcon.HTTP_401)

        req.context = User.User(username)
        if not(req.context.is_auth(req)):
            raise falcon.HTTPStatus(falcon.HTTP_401)

app = falcon.asgi.App(middleware=[AuthMiddleware()])

falcon.RequestOptions.strip_url_path_trailing_slash = True

app.add_route('/v1', Info.Info())
app.add_route('/v1/users', Users.Users())
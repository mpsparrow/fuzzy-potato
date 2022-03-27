import falcon

class Access:
    def __init__(self, roles: list):
        self.roles = roles

    async def __call__(self, req, resp, resource, params):
        user_roles = req.context.get_roles()
        is_allowed = False

        for role in self.roles:
            if role in user_roles:
                is_allowed = True
        
        if not(is_allowed):
            raise falcon.HTTPStatus(falcon.HTTP_403)
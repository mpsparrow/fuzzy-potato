class User:
    def __init__(self, username):
        self.username = username

    def sync(self):
        '''
        Syncs users changes with database.
        '''

    def get_username(self):
        '''
        Gets users username.

        :return str: Username
        '''
        
    def get_userid(self):
        '''
        Gets user ID.

        :return int: User ID
        '''

    def check_password(self, password):
        '''
        
        '''

    def is_auth(self, req):
        '''
        '''
        return True

    def get_roles(self):
        '''
        
        '''
        return ['admin']
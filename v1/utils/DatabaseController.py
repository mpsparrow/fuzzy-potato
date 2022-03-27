'''
Defines the Project class.

Description
-----------
Defines the base class DatabaseController for controlling database connections.

Changelog
---------
- Created by mpsparrow on 2022/03/24.
'''

import pymongo

class DatabaseController:
    '''
    DatebaseController base class.
    
    For controlling database connections.
    '''

    def __init__(self, credentials: str):
        '''
        DatabaseController base class initializer.

        :param credentials str: URL credential string for MongoDB  
        '''
        self.credentials = credentials
        self.cursor = None

    def open(self):
        '''
        Open the database connection.
        '''
        self.cursor = pymongo.MongoClient(self.credentials)

    def get_cursor(self):
        '''
        :return MongoClient: MongoClient
        '''
        return self.cursor

    def close(self):
        '''
        Close the database connection.
        '''
        self.cursor.close()

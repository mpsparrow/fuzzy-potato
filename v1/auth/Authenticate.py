from passlib.context import CryptContext
from ..utils import DatabaseController

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

class Authenticate:
    '''
    
    '''
    def user_lookup(self, username):
        '''
        
        '''
        cursor = DatabaseController.DatabaseController()


    def check_password(self, password, hash):
        '''
        '''
        return pwd_context.verify(password, hash)

    async def on_post(self, req, resp):
        '''
        '''
        
def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

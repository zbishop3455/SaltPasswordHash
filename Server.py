
from os import urandom
from hashlib import sha512
import bcrypt

class Server:
    def __init__(self):
        # Database format: db[username] = ( salt, hashed )
        self.user_authentication_database = {}
        self.hash_alg = sha512()
        print("Created new server representation")

    # store raw user data
    def add_user(self, username, salt, hashed):
        self.user_authentication_database[username] = [salt, hashed]

    # store user data with a hash
    def add_user_secure(self, username, salt, hashed):
        self.hash_alg.update(hashed)
        safe_hash = self.hash_alg.digest()
        self.hash_alg.update(salt)
        safe_salt = self.hash_alg.digest()

        self.user_authentication_database[username] = [safe_salt, safe_hash]

    # store user data with b-crypt
    def add_user_super_secure(self, username, salt, hash):
        pass

    # return user salt
    def get_user_salt(self, username):
        user_data = self.user_authentication_database[username]
        return user_data[0]

    def authenticate(self, username, hash_guess):
        user_data = self.user_authentication_database[username]
        if user_data[1] == hash_guess:
            return True
        else:
            return False



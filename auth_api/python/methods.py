from hashlib import sha512
import jwt
import os

JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = 'HS256'

class Token:
    def generate_token(self, username):
        payload = {'sub': username }
        return jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)     

class Restricted:
    def access_data(self, authorization):
        try:
            payload = jwt.decode(authorization, JWT_SECRET, JWT_ALGORITHM)
            return "You are under protected data"
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again'

class SHA512:
    def verify(self, expected_hash, password, salt):
        composed_pass = password + salt
        generated_hash = sha512(composed_pass.encode('utf-8').strip()).hexdigest()
        return generated_hash == expected_hash
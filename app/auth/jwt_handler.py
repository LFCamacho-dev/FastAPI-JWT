import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# This function returns generated Tokens (JWTs)
def token_response(token: str):
    return {
        "access token": token
    }

 
# This function is used for signing the JWT string   
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600,
    }  
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)


# This function is used to decode the token
def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
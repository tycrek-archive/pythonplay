# rhash.py
import base64

def rhash(s):
    return base64.b64encode(str.encode(s)).decode()

def un_rhash(s):
    return base64.b64decode(str.encode(s)).decode()
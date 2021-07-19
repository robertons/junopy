
from junopy.utils.juno import *

import hmac
import hashlib

def Banks():
    data = Get("/data/banks")
    return data['_embedded']['banks']

def CompanyTypes():
    data = Get("/data/company-types")
    return data['companyTypes']

def BusinessAreas():
    data = Get("/data/business-areas")
    return data['_embedded']['businessAreas']

def PublicKey(resourceToken=None):
    data = Get("/credentials/public-key", {'resourceToken': resourceToken})
    return data

def IsValidWebhook(x_signature:str, body:bytes, secret:str):
    secret = secret.encode('utf-8')
    digest = hmac.HMAC(secret, body, hashlib.sha256).hexdigest()
    return digest == x_signature

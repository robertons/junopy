
from junopy.utils.juno import *


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

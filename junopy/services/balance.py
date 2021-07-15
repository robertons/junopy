
from junopy.utils.juno import *


def Balance(resourceToken=None):
    if resourceToken is None:
        data = Get("/balance")
    else:
        data = Get("/balance", {'resourceToken': resourceToken})
    del data['_links']
    return data

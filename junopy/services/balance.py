
from junopy.utils.juno import *


def Balance(resourceToken=None):
    if resourceToken is None:
        data = Get("/balance")
    else:
        data = Get("/balance", {'resourceToken': resourceToken})
    try:
        del data['_links']
    except Exception as e:
        pass
    return data

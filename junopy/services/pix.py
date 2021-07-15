
from junopy.utils.juno import *
from junopy import Pix


def Keys(idempotency: str, type: str = "RANDOM_KEY", key: str = ""):

    req_data = {'type': type}

    if type == "RANDOM_KEY" and key != "":
        req_data['key'] = key

    print(req_data)
    data = Post("/pix/keys", req_data, {'X-Idempotency-Key': idempotency})
    print(data)
    return Pix(**data)


def StaticQRCode(idempotency: str, key: str, includeImage: bool = False, amount: float = 0, reference: str = '', additionalData: str = ''):

    req_data = {
        'key': key,
        'includeImage': includeImage
    }

    if amount > 0:
        req_data['amount'] = amount

    if reference != '':
        req_data['reference'] = reference

    if additionalData != '':
        req_data['additionalData'] = additionalData

    data = Post("/pix/qrcodes/static", req_data, {'X-Idempotency-Key': idempotency})
    print(data)
    return Pix(**data)

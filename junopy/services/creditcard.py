
from junopy.utils.juno import *
from junopy import CreditCard


def Tokenize(hash: str):
    data = Post("/credit-cards/tokenization", {
        'creditCardHash': hash
    })
    data['creditCardHash'] = hash
    return CreditCard(**data)

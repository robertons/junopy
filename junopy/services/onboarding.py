
from junopy.utils.juno import *
from junopy import Onboarding

def Documents(returnUrl:str, refreshUrl:str, emailOptOut:bool=False):
    data = Post("/onboarding/link-request", {
        'type': 'DOCUMENTS_UPLOAD',
        'emailOptOut' : emailOptOut,
        'returnUrl':returnUrl,
        'refreshUrl': refreshUrl
    })
    return Onboarding(**data)


def Account(returnUrl:str, refreshUrl:str, referenceId=None, autoTransfer:bool=False, emailOptOut:bool=False):
    data = Post("/onboarding/link-request", {
        "type": "SIGNUP",
        "referenceId": referenceId,
        "autoTransfer": autoTransfer,
        "emailOptOut": emailOptOut,
        "returnUrl": returnUrl,
        "refreshUrl": refreshUrl
    })
    return Onboarding(**data)

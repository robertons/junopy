
from junopy.utils import constants
import base64
from requests_toolbelt import MultipartEncoder
import requests
import logging
import json
import os
import io

DEBUG = False
TOKEN = {}
SANDBOX = True
CLIENTID = ''
CLIENTSECRET = ''


def DebugRequest():
    import http.client as http_client
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def Juno(private_token, clientId, clientSecret, sandbox=True, debug=False):
    if debug:
        DebugRequest()
    global DEBUG
    global TOKEN
    global SANDBOX
    global CLIENTID
    global CLIENTSECRET
    DEBUG = debug
    SANDBOX = sandbox
    CLIENTID = clientId
    CLIENTSECRET = clientSecret
    TOKEN['PRIVATE'] = private_token


def GetToken():
    hash = base64.b64encode(f'{CLIENTID}:{CLIENTSECRET}'.encode("utf-8")).decode("utf-8")
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {hash}'
    }
    route = constants.ROUTE_SANDBOX_AUTORIZATION_SERVER if SANDBOX else constants.ROUTE_PRODUCAO_AUTORIZATION_SERVER
    response = __ValidateResponse(requests.post(
        route, headers=headers, data={'grant_type': 'client_credentials'}))
    TOKEN['TOKEN'] = response['access_token']
    TOKEN['TYPE'] = response['token_type']
    TOKEN['EXPIRES'] = response['expires_in']


def __headers(data=None, aditional_header=None):

    resource_token = data['resourceToken'] if data and 'resourceToken' in data else None
    if resource_token is None:
        resource_token = aditional_header['resourceToken'] if aditional_header and 'resourceToken' in aditional_header else None

    if not 'TYPE' in TOKEN or not 'TOKEN' in TOKEN or not 'EXPIRES' in TOKEN:
        GetToken()

    __headers = {
        'Content-Type': 'application/json;charset=UTF-8' if aditional_header is None or not 'Content-Type' in aditional_header else aditional_header['Content-Type'],
        'X-Api-Version': '2',
        'X-Resource-Token': f"{TOKEN['PRIVATE'] if resource_token is None else resource_token}",
        'Authorization': f"{TOKEN['TYPE']} {TOKEN['TOKEN']}"
    }
    if not aditional_header is None:
        __headers = {**__headers, **aditional_header}

    return __headers


def __Route(url):
    route = constants.ROUTE_SANDBOX if SANDBOX else constants.ROUTE_PRODUCAO
    return f'{route}{url}'


def Get(url, data={}, aditional_header=None):
    return __ValidateResponse(requests.get(__Route(url), params=data, headers=__headers(data, aditional_header)))


def Post(url, data, aditional_header=None):
    return __ValidateResponse(requests.post(__Route(url), json=data, headers=__headers(data, aditional_header)))


def Put(url, data, aditional_header=None):
    return __ValidateResponse(requests.put(__Route(url), json=data, headers=__headers(data, aditional_header)))


def Patch(url, data, aditional_header=None):
    post_data = dict(data)
    if 'resourceToken' in post_data:
        del post_data['resourceToken']
    return __ValidateResponse(requests.patch(__Route(url), json=post_data, headers=__headers(data, aditional_header)))


def Delete(url, aditional_header=None):
    return __ValidateResponse(requests.delete(__Route(url), headers=__headers(None, aditional_header)))


def UploadMultiPart(url, files, data=None, aditional_header=None):
    f = []
    for file in files:
        if isinstance(file, str):
            f.append(('files', (file, open(file, 'rb'))))
        elif isinstance(file, tuple) and isinstance(file[0], str) and (isinstance(file[1], bytes) or isinstance(file[1], io.BufferedReader)):
            f.append(('files', (file[0], file[1])))
    m = MultipartEncoder(fields=f)
    return __ValidateResponse(requests.post(__Route(url), data=m, headers=__headers(data, {'Content-Type': m.content_type})))


class JunoException(Exception):
    def __init__(self, message, detail):
        self.message = message
        self.detail = detail


def __ValidateResponse(response):

    if response.status_code == 200:
        try:
            if DEBUG:
                print(f"Response:\n\n {json.dumps(response.json(), indent=4)} \n\n")
            return response.json()
        except:
            if DEBUG:
                print(f"Response:\n\n {response.text} \n\n")
            return response.text
    elif response.status_code == 204:
        # RESPONSE OK - NO CONTENT
        return None
    elif response.status_code > 204:
        status_code = response.status_code
        try:
            response_json = response.json()
        except Exception as e:
            response_json = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": status_code,
                "error": "Internal Server Error",
                "details": [
                    {
                        "message": str(e),
                        "errorCode": "0"
                    }
                ]
            }
        raise JunoException("Juno Request Error", response_json)

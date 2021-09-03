
from junopy.utils.juno import *
from junopy import EventType, Webhook
from junopy.entities.lib.datatype import ListType


def EventTypes():
    data = Get("/notifications/event-types")
    return ListType(EventType).add([EventType(**item) for item in data['_embedded']['eventTypes']]) if '_embedded' in data else ListType(EventType)


def Webhooks(resourceToken=None):
    aditional_header = None
    if not resourceToken is None:
        aditional_header = {'resourceToken':resourceToken}
    data = Get("/notifications/webhooks", aditional_header=aditional_header)
    return ListType(Webhook).add([Webhook(**item) for item in data['_embedded']['webhooks']]) if '_embedded' in data else ListType(Webhook)

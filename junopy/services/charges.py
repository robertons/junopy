
from junopy.utils import juno
from junopy import Charge, ChargeResource, Billing, Split


from junopy.entities.lib.datatype import ListType

_prev_search = ''
_next_search = ''


def Create(charge: Charge, billing: Billing):
    data = juno.Post("/charges", {
        'charge': charge.toJSON(),
        'billing': billing.toJSON()
    })
    return ListType(ChargeResource).add([ChargeResource(**item) for item in data['_embedded']['charges']]) if '_embedded' in data else ListType(ChargeResource)


def Get(id: str):
    data = juno.Get(f"/charges/{id}")
    return ChargeResource(**data)


def Cancel(id: str):
    data = juno.Put(f"/charges/{id}/cancelation", {})
    return None


def SetSplit(id: str, split: list):
    data = juno.Put(
        f"/charges/{id}/split", {'split': [item if isinstance(item, dict) else item.toJSON() for item in split]})
    return None


def SetLinks(data):
    _next_search = data['_links']['next']['href'] if '_links' in data and 'next' in data['_links'] else ''
    _prev_search = data['_links']['previous']['href'] if '_links' in data and 'previous' in data['_links'] else ''


def Search(**kw):
    data = juno.Get("/charges", kw)
    SetLinks(data)
    return ListType(ChargeResource).add([ChargeResource(**item) for item in data['_embedded']['charges']]) if '_embedded' in data else ListType(ChargeResource)


def Next():
    if _next_search != '':
        data = juno.Get(_next_search, kw)
        SetLinks(data)
        return ListType(ChargeResource).add([ChargeResource(**item) for item in data['_embedded']['charges']]) if '_embedded' in data else ListType(ChargeResource)
    else:
        return ListType(ChargeResource)


def Previous():
    if _next_search != '':
        data = juno.Get(_next_search, kw)
        SetLinks(data)
        return ListType(ChargeResource).add([EventType(**item) for item in data['_embedded']['charges']]) if '_embedded' in data else ListType(ChargeResource)
    else:
        return ListType(ChargeResource)

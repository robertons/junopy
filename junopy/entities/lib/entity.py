# -*- coding: utf-8 -*-

from .datatype import *
from junopy.utils.juno import *

__methods__ = ['toJSON', 'load', 'add', 'Create', 'Update', 'Get',
               'Delete', 'Deactivate', 'Reactivate', 'Cancel', 'Complete', 'SendFiles']


def EncodeValue(o, format=None):
    try:
        if hasattr(o, 'toJSON'):
            return o.toJSON()
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, datetime.datetime):
            return o.strftime(format) if format != 'iso' else o.isoformat()
        if isinstance(o, bytes):
            return o.decode('utf-8')
        return o
    except Exception as e:
        raise e


class JunoEntity():

    def __init__(self, aliases=None, context=None, **kw):
        self.__metadata__['data'] = {}
        self.__metadata__['relasionships'] = {}
        self.__context__ = context
        self.load(**kw)

    def load(self, **kw):
        if len(kw) > 0:
            for k in self.__dict__:
                try:
                    if not k.startswith("__"):
                        if k in kw:
                            if self[k].__class__.__name__.startswith("Obj"):
                                self.add(k, kw[k])
                            else:
                                self[k].value = kw[k]
                                self.__metadata__['data'][k] = EncodeValue(
                                    self[k].value, self[k].format)
                except Exception as e:
                    raise Exception(f"Field [{k}] Value [{kw[k]}] Error : {e}")

    def add(self, key=None, data=None):
        if key and data and (isinstance(data, dict) or isinstance(data, list)):
            if "List" in self[key].__class__.__name__:
                if not key in self.__metadata__['relasionships']:
                    self.__metadata__['relasionships'][key] = []
                self.__metadata__['relasionships'][key].extend(
                    data if isinstance(data, list) else [data])

                if hasattr(data, 'values'):

                    self[key].value.extend([self[key].type(context={'entity': self, 'key': key}, **item) for item in data if any(item.values(
                    ))] if isinstance(data, list) else [self[key].type(context={'entity': self, 'key': key}, **data)] if any(data.values()) else [])

                elif isinstance(data, list):
                    self[key].value.extend([self[key].type(item) if isinstance(item, str) or isinstance(
                        item, int) else self[key].type(context={'entity': self, 'key': key}, **item) for item in data if not item is None])
            else:
                data = data[0] if isinstance(data, list) else data
                if any(data.values()):
                    self.__metadata__['relasionships'][key] = data
                    self[key].value = self[key].type(context={'entity': self, 'key': key}, **data)
        elif hasattr(data, '__class__') and data.__class__.__name__ == self[key].type.__name__:
            self.__setattr__(key, data)
        else:
            raise Exception("entity.add requires key and dict of object data")

    def __getitem__(self, field):
        return super().__getattribute__(field) if hasattr(self, field) else None

    def __getattribute__(self, field):
        if field.startswith("__") or field in __methods__:
            return super().__getattribute__(field)
        else:
            return super().__getattribute__(field).value

    def __setattr__(self, item, value):
        try:
            if not item.startswith("__") and not "entity.datatype" in str(value.__class__):
                if self[item]:
                    if hasattr(value, '__context__') and not value.__context__:
                        value.__context__ = self
                    self[item].value = value
                    self.__metadata__['data'][item] = EncodeValue(
                        self[item].value, self[item].format)
                    if self.__context__:
                        _context = self.__context__['entity']
                        _context_key = self.__context__['key']
                        if isinstance(_context[_context_key].value, list):
                            index = _context[_context_key].value.index(self)
                            _context.__metadata__[
                                'relasionships'][_context_key][index] = self.__metadata__['data']
                        else:
                            _context.__metadata__[
                                'relasionships'][_context_key] = self.__metadata__['data']
                else:
                    super().__setattr__(item, value)
            else:
                super().__setattr__(item, value)
        except Exception as e:
            raise Exception(f"Field [{item}] Value [{value}] Error : {e}")

    def toJSON(self):
        try:
            return {**self.__metadata__['data'], **self.__metadata__['relasionships']}
        except Exception as e:
            raise e

    def Create(self):
        if hasattr(self, '__route__'):
            data = Post(self.__route__, self.toJSON())
            self.load(**data)
        else:
            raise Exception("Method Create not allowed this object")
        return self

    def Update(self):
        if hasattr(self, '__route__'):
            route = self.__route__
            if hasattr(self, '__requireid__'):
                if self.__requireid__ == True and self.id is None:
                    raise Exception("ID object required")
                if self.id is not None:
                    route = f"{route}/{self.id}"
                    self.id = None
            data = Patch(route, self.toJSON())
            self.load(**data)
        else:
            raise Exception("Method Update not allowed this object")
        return self

    def Get(self):
        if hasattr(self, '__route__'):
            route = self.__route__
            if hasattr(self, '__requireid__'):
                if self.__requireid__ == True and self.id is None:
                    raise Exception("ID object required")
                route = f"{route}/{self.id}"
            data = Get(route, {'resourceToken': self.resourceToken} if hasattr(
                self, 'resourceToken') and not self.resourceToken is None else None)
            self.load(**data)
        else:
            raise Exception("Method Get not allowed this object")
        return self

    def Delete(self):
        if hasattr(self, '__route__'):
            route = self.__route__
            if hasattr(self, '__requireid__') and self.__requireid__ == True:
                if self.id is None:
                    raise Exception("ID object required")
                route = f"{route}/{self.id}"
            Delete(route)
        else:
            raise Exception("Method Delete not allowed this object")
        self = None
        return None

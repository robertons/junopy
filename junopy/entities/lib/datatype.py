# -*- coding: utf-8 -*-

import decimal
import datetime


class ValidateValue:

    def __init__(self, default=None, context=None, required=False, max=None, name=None, type=None, format=None, key=None):
        self.scale = 2
        self.context = context
        self.required = required
        self.max = max
        self.name = name
        if name:
            if name == 'str':
                self.type = str
            elif name == 'int':
                self.type = int
            else:
                self.type = getattr(__import__(
                    f'junopy.entities.{name.lower()}', fromlist=[name]), name)
        else:
            self.type = None
        self.format = format
        self.key = key
        self._value = None if not self.__class__ or not 'List' in self.__class__.__name__ else ListType(
            self.type, context, key)
        if self._value is None and default is not None:
            self._value = default

    def __call__(self, **kw):
        if self.type:
            return self.type(**kw)
        else:
            raise Exception(f"TypeError '{self.name}' object is not callable")

    def __reset__(self):
        self._value = None if not self.__class__ or not 'List' in self.__class__.__name__ else ListType(
            self.type, self.context, self.key)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class String(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if not isinstance(data, str):
                raise Exception("requires string")
            if self.max and len(data) > self.max:
                raise Exception(f"Value too large. The default limit is {self.max}")
        super().__setattr__(attr, data)


class Int(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if self.max and len(str(data)) > self.max:
                raise Exception(f"Value too large. The default limit is {self.max}")
            if not isinstance(data, int):
                try:
                    data = int(data)
                except ValueError as e:
                    raise Exception("requires int")
        super().__setattr__(attr, data)


class DateTime(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if not isinstance(data, datetime.datetime):
                try:
                    if self.format != 'iso':
                        data = datetime.datetime.strptime(data, self.format)
                    else:
                        data = datetime.datetime.fromisoformat(data)

                except ValueError as e:
                    if "unconverted data remain" not in str(e):
                        raise Exception(
                            f"is not datetime or string is not correct format, expected [{self.format}]")
                    pass
        super().__setattr__(attr, data)


class Decimal(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if not isinstance(data, Decimal):
                try:
                    data = decimal.Decimal(str(round(float(data), self.scale)))
                except ValueError as e:
                    raise Exception("requires Decimal")
        super().__setattr__(attr, data)


class Float(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if not isinstance(data, float):
                try:
                    if self.scale:
                        data = round(float(data), self.scale)
                    else:
                        data = float(data)
                except ValueError as e:
                    raise Exception("requires Float")
        super().__setattr__(attr, data)


class Boolean(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if not isinstance(data, bool):
                try:
                    data = bool(data)
                except ValueError as e:
                    raise Exception("requires Boolean")
        super().__setattr__(attr, data)


class Dict(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if not isinstance(data, dict):
                raise Exception("requires Dict")
        super().__setattr__(attr, data)


class Obj(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            if data.__class__.__name__ != self.type.__name__:
                raise Exception(f"requires {self.type.__name__} object")
        super().__setattr__(attr, data)


class ObjList(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data, check=True):
        if check and attr == "value" and data is not None:
            self.value.add(data)
        super().__setattr__(attr, data)


class ListType(list):

    def __init__(self, type, _context=None, key=None):
        self._type = type
        self._context = _context
        self._key = key
        super(ListType, self).__init__()

    def append(self, item):
        try:

            if not isinstance(item, set) and not isinstance(item, map) and not isinstance(item, list) and item.__class__.__name__ != self._type.__name__:
                raise Exception(f'Item type not is {self._type.__name__}')

            if self._context and not self._key in self._context.__metadata__['relasionships']:
                self._context.__metadata__['relasionships'][self._key] = []

            if isinstance(item, list):
                super(ListType, self).extend(item)
                if (self._context):
                    self._context.__metadata__['relasionships'][self._key].extend(self.toJSON())
            elif isinstance(item, set) or isinstance(item, map):
                super(ListType, self).extend(list(item))
                if (self._context):
                    self._context.__metadata__['relasionships'][self._key].extend(self.toJSON())
            else:
                super(ListType, self).append(item)
                if (self._context):
                    self._context.__metadata__['relasionships'][self._key].append(item.toJSON())

        except Exception as e:
            raise e
        return self

    def add(self, item):
        self.append(item)
        return self

    def toJSON(self):
        try:
            return [item.toJSON() if hasattr(item, "toJSON") else item for item in self]
        except Exception as e:
            raise e

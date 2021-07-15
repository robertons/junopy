# -*- coding: utf-8 -*-
from .lib import *
from junopy.entities.lib.datatype import ListType


class Plan(JunoEntity):

    def __init__(cls, **kw):

        cls.__route__ = '/plans'
        cls.__requireid__ = False
        cls.__metadata__ = {}

        # FIELDS
        cls.id = String(max=80)
        cls.createdOn = DateTime(format="iso")
        cls.name = String(max=100)
        cls.frequency = String(default="MONTHLY", max=100)
        cls.status = String(max=30)
        cls.amount = Float()

        super().__init__(**kw)

    def Get(self):
        if self.id:
            route = f"{self.__route__}/{self.id}"
            data = Get(route, None)
            self.load(**data)
            return self
        else:
            data = Get(self.__route__, None)
            _type = getattr(__import__('junopy.entities.plan', fromlist=['Plan']), 'Plan')
            return ListType(_type).add([_type(**item) for item in data['_embedded']['plans']]) if '_embedded' in data else ListType(_type)

    def Deactivate(self):
        data = Post(f"{self.__route__}/{self.id}/deactivation", self.toJSON())
        self.load(**data)
        return self

    def Reactivate(self):
        data = Post(f"{self.__route__}/{self.id}/activation", self.toJSON())
        self.load(**data)
        return self

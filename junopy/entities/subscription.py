# -*- coding: utf-8 -*-
from .lib import *
from junopy.entities.lib.datatype import ListType


class Subscription(JunoEntity):

    def __init__(cls, **kw):

        cls.__route__ = '/subscriptions'
        cls.__requireid__ = False
        cls.__metadata__ = {}

        # FIELDS
        cls.id = String(max=80)
        cls.createdOn = DateTime(format="iso")
        cls.planId = String(max=80)
        cls.dueDay = Int()
        cls.chargeDescription = String(max=200)
        cls.creditCardDetails = Obj(context=cls, key='creditCardDetails', name='CreditCard')
        cls.billing = Obj(context=cls, key='billing', name='Billing')
        cls.split = ObjList(context=cls, key='split', name='Split')
        cls.status = String(max=30)
        cls.startsOn = DateTime(format="%Y-%m-%d")
        cls.lastBillingDate = DateTime(format="%Y-%m-%d")
        cls.nextBillingDate = DateTime(format="%Y-%m-%d")

        super().__init__(**kw)

    def Get(self):
        if self.id:
            route = f"{self.__route__}/{self.id}"
            data = Get(route, None)
            self.load(**data)
            return self
        else:
            data = Get(self.__route__, None)
            _type = getattr(__import__('junopy.entities.subscription', fromlist=['Subscription']), 'Subscription')
            return ListType(_type).add([_type(**item) for item in data['_embedded']['subscriptions']]) if '_embedded' in data else ListType(_type)

    def Deactivate(self):
        data = Post(f"{self.__route__}/{self.id}/deactivation", self.toJSON())
        self.load(**data)
        return self

    def Reactivate(self):
        data = Post(f"{self.__route__}/{self.id}/activation", self.toJSON())
        self.load(**data)
        return self

    def Cancel(self):
        data = Post(f"{self.__route__}/{self.id}/cancelation", self.toJSON())
        self.load(**data)
        return self

    def Complete(self):
        data = Post(f"{self.__route__}/{self.id}/completion", self.toJSON())
        self.load(**data)
        return self

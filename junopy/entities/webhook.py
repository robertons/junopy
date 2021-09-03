# -*- coding: utf-8 -*-
from .lib import *

class Webhook(JunoEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/notifications/webhooks'
		cls.__requireid__ = True
		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=80)
		cls.url = String(max=200)
		cls.secret = String(max=200)
		cls.status = String(max=30)
		cls.eventTypes = ObjList(context=cls, key='eventTypes', name='EventType')

		super().__init__(**kw)

	def Create(self, url:str, eventTypes:list, resourceToken=None):
		aditional_header = None
		if not resourceToken is None:
			aditional_header = {'resourceToken':resourceToken}
		data = Post(self.__route__, {
			'url':url,
			'eventTypes':eventTypes
		}, aditional_header)
		self.load(**data)
		return self

	def Delete(self, resourceToken=None):
		aditional_header = None
		if not resourceToken is None:
			aditional_header = {'resourceToken':resourceToken}
		if hasattr(self, '__route__'):
			route = self.__route__
			if hasattr(self, '__requireid__') and self.__requireid__ == True:
				if self.id is None:
					raise Exception("ID object required")
				route = f"{route}/{self.id}"
			Delete(route, aditional_header=aditional_header)
		else:
			raise Exception("Method Delete not allowed this object")
		self = None
		return None

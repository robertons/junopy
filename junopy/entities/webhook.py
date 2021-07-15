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

	def Create(self, url:str, eventTypes:list):
		data = Post(self.__route__, {
			'url':url,
			'eventTypes':eventTypes
		})
		self.load(**data)
		return self

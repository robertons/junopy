# -*- coding: utf-8 -*-
from .lib import *

class Billing(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.name = String(max=80)
		cls.document = String(max=14)
		cls.email = String(max=80)
		cls.address = Obj(context=cls, key='address', name='Address')
		cls.secondaryEmail = String(max=80)
		cls.phone = String(max=25)
		cls.birthDate = DateTime(format="%Y-%m-%d")
		cls.notify = Boolean(default=False)
		cls.delayed = Boolean()

		super().__init__(**kw)

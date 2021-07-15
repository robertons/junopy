# -*- coding: utf-8 -*-
from .lib import *

class Address(JunoEntity):

	def __init__(cls, **kw):
		
		cls.__metadata__ = {}

		# FIELDS
		cls.street = String(max=100, required=True)
		cls.number = String(max=10, required=True)
		cls.complement = String(max=20)
		cls.neighborhood = String(max=20)
		cls.city = String(max=20, required=True)
		cls.state = String(max=20, required=True)
		cls.postCode = String(max=8, required=True)

		super().__init__(**kw)

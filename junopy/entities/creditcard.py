# -*- coding: utf-8 -*-
from .lib import *

class CreditCard(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.creditCardHash = String(required=True)
		cls.creditCardId = String(required=True)
		cls.last4CardNumber = String(required=True)
		cls.expirationMonth = String(required=True)
		cls.expirationYear = String(required=True)

		super().__init__(**kw)

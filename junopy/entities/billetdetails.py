# -*- coding: utf-8 -*-
from .lib import *

class BilletDetails(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.bankAccount = String(required=True)
		cls.ourNumber = String(required=True)
		cls.barcodeNumber = String(required=True)
		cls.portfolio = String(required=True)

		super().__init__(**kw)

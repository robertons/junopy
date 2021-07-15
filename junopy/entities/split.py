# -*- coding: utf-8 -*-
from .lib import *

class Split(JunoEntity):

	def __init__(cls, **kw):
		
		cls.__metadata__ = {}

		# FIELDS
		cls.recipientToken = String(max=80)
		cls.amount = Float()
		cls.percentage = Float()
		cls.amountRemainder = Boolean()
		cls.chargeFee = Boolean()

		super().__init__(**kw)

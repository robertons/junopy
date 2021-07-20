# -*- coding: utf-8 -*-
from .lib import *

class Payment(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=80)
		cls.chargeId = String(max=100)
		cls.date = DateTime(format="iso")
		cls.releaseDate = DateTime(format="iso")
		cls.amount = Float()
		cls.fee = Float()
		cls.type = String(max=30)
		cls.status = String(max=30)
		cls.transactionId = String(max=30)
		cls.failReason = String(max=30)

		super().__init__(**kw)

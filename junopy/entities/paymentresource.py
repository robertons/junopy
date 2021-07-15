# -*- coding: utf-8 -*-
from .lib import *

class PaymentResource(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.transactionId = String(max=80)
		cls.installments = Int()
		cls.payments = ObjList(context=cls, key='payments', name='Payment')
		cls.refunds = ObjList(context=cls, key='refunds', name='Refund')

		super().__init__(**kw)

# -*- coding: utf-8 -*-
from .lib import *

class Transfer(JunoEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/transfers'
		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=80)
		cls.type = String(default="DEFAULT_BANK_ACCOUNT", required=True)
		cls.name = String(max=80, required=True)
		cls.document = String(max=14, required=True)
		cls.amount = Float()
		cls.bankAccount = Obj(context=cls, key='bankAccount', name='BankAccount')
		cls.creationDate = DateTime(format="iso")
		cls.transferDate = DateTime(format="iso")
		cls.digitalAccountId = String(max=80, required=True)
		cls.status = String(max=40)
		cls.recipient = Obj(context=cls, key='recipient', name='Recipient')
		
		super().__init__(**kw)

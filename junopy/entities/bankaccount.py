# -*- coding: utf-8 -*-
from .lib import *

class BankAccount(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.ispb = String(max=10)
		cls.bankNumber = String(max=3, required=True)
		cls.agencyNumber = String(max=10, required=True)
		cls.accountNumber = String(max=20, required=True)
		cls.accountComplementNumber = String(max=3, required=True)
		cls.accountType = String(max=10, required=True)
		cls.accountHolder = Obj(context=cls, key='accountHolder', name='AccountHolder')

		super().__init__(**kw)

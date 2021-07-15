# -*- coding: utf-8 -*-
from .lib import *

class Recipient(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.name = String(max=80, required=True)
		cls.document = String(max=14, required=True)
		cls.bankAccount = Obj(context=cls, key='bankAccount', name='BankAccount')
		
		super().__init__(**kw)

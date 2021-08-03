# -*- coding: utf-8 -*-
from .lib import *

class Charge(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.pixKey = String(max=160)
		cls.pixIncludeImage = Boolean(default=False, required=True)
		cls.description = String(max=80)
		cls.references = ObjList(context=cls, key='references', name='str')
		cls.totalAmount = Float()
		cls.amount = Float(required=True)
		cls.dueDate =  DateTime(format="%Y-%m-%d")
		cls.installments = Int()
		cls.maxOverdueDays = Int()
		cls.fine = Int()
		cls.interest = Decimal()
		cls.discountAmount = Decimal()
		cls.discountDays = Int()
		cls.paymentTypes = ObjList(context=cls, key='paymentTypes', name='str')
		cls.paymentAdvance = Boolean()
		cls.feeSchemaToken = String(max=80)
		cls.split = ObjList(context=cls, key='split', name='Split')

		super().__init__(**kw)

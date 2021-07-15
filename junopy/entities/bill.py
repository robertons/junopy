# -*- coding: utf-8 -*-
from .lib import *

class Bill(JunoEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/bill-payments'
		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=80)
		cls.digitalAccountId = String(max=100)
		cls.billType = ObjList(context=cls, key='status', name='str')
		cls.numericalBarCode = String(max=100)
		cls.paymentDescription = String(max=100)
		cls.beneficiaryDocument = String(max=100)
		cls.dueDate = DateTime(format="%Y-%m-%d")
		cls.paymentDate = DateTime(format="%Y-%m-%d")
		cls.billAmount = Float()
		cls.paidAmount =Float()
		cls.createdOn = DateTime(format="iso")
		cls.status = ObjList(context=cls, key='status', name='str')

		super().__init__(**kw)

# -*- coding: utf-8 -*-
from .lib import *

class ChargeResource(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=80)
		cls.code = Int()
		cls.reference = String(max=80)
		cls.dueDate = DateTime(format="iso")
		cls.link = String()
		cls.checkoutUrl = String(max=200)
		cls.installmentLink = String(max=200)
		cls.payNumber = String(max=100)
		cls.amount = Float()
		cls.status= String(max=30)
		cls.billetDetails = Obj(context=cls, key='billetDetails', name='BilletDetails')
		cls.payments = ObjList(context=cls, key='payments', name='Payment')
		cls.subscription = ObjList(context=cls, key='subscription', name='Subscription')
		cls.pix = Obj(context=cls, key='pix', name='Pix')
		cls.imageInBase64 = String(max=80)

		super().__init__(**kw)

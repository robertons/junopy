# -*- coding: utf-8 -*-
from .lib import *

class DigitalAccount(JunoEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/digital-accounts'
		cls.__requireid__ = False
		cls.__metadata__ = {}

		# FIELDS
		cls.id =  String(max=80)
		cls.status =  String(max=40)
		cls.createdOn = DateTime(format="iso")
		cls.resourceToken = String(max=200)
		cls.personType = String(max=10)
		cls.type = String(default="PAYMENT", required=True)
		cls.name = String(max=80, required=True)
		cls.motherName  = String(max=80, required=True)
		cls.document = String(max=14, required=True)
		cls.email = String(max=80, required=True)
		cls.birthDate = DateTime(format="%Y-%m-%d")
		cls.phone = String(max=16, required=True)
		cls.businessArea = Int(max=4)
		cls.linesOfBusiness = String(max=100)
		cls.companyType = String(max=28, required=True)
		cls.legalRepresentative = Obj(context=cls, key='legalRepresentative', name='LegalRepresentative')
		cls.address = Obj(context=cls, key='address', name='Address')
		cls.bankAccount = Obj(context=cls, key='bankAccount', name='BankAccount')
		cls.emailOptOut = Boolean(default=False)
		cls.autoTransfer = Boolean(default=False)
		cls.socialName = Boolean(default=False)
		cls.monthlyIncomeOrRevenue = Int()
		cls.cnae = String(max=7)
		cls.establishmentDate = DateTime(format="%Y-%m-%d")
		cls.pep = Boolean(default=False)
		cls.companyMembers = ObjList(context=cls, key='companyMembers', name='CompanyMembers')

		super().__init__(**kw)

# -*- coding: utf-8 -*-
from .lib import *

class CompanyMembers(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.name = String(max=80, required=True)
		cls.document = String(max=14, required=True)
		cls.birthDate = DateTime(format="%Y-%m-%d")

		super().__init__(**kw)

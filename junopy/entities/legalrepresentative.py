# -*- coding: utf-8 -*-
from .lib import *

class LegalRepresentative(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.name = String(max=80, required=True)
		cls.document = String(max=14, required=True)
		cls.birthDate = DateTime(format="%Y-%m-%d")
		cls.motherName = String(max=80, required=True)
		cls.type = String(default="INDIVIDUAL", required=True)

		super().__init__(**kw)

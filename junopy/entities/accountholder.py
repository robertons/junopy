# -*- coding: utf-8 -*-
from .lib import *

class AccountHolder(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.name = String(max=80, required=True)
		cls.document = String(max=14, required=True)

		super().__init__(**kw)

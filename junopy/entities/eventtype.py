# -*- coding: utf-8 -*-
from .lib import *

class EventType(JunoEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=80)
		cls.name = String(max=80)
		cls.label = String(max=80)
		cls.status = String(max=80)

		super().__init__(**kw)

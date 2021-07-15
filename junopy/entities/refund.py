# -*- coding: utf-8 -*-
from .lib import *


class Refund(JunoEntity):

    def __init__(cls, **kw):

        cls.__metadata__ = {}

        # FIELDS
        cls.id = String(max=80)
        cls.chargeId = String(max=80)
        cls.releaseDate = DateTime(format="iso")
        cls.paybackDate = DateTime(format="iso")
        cls.paybackAmount = Float(),
        cls.status = String(max=40)

        super().__init__(**kw)

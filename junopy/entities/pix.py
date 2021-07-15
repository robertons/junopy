# -*- coding: utf-8 -*-
from .lib import *


class Pix(JunoEntity):

    def __init__(cls, **kw):

        cls.__metadata__ = {}

        # FIELDS
        cls.id = String(max=80)
        cls.key = String(max=80)
        cls.type = String(max=80)
        cls.includeImage = Boolean()
        cls.payloadInBase64 = String()
        cls.imageInBase64 = String()
        cls.qrcodeInBase64 = String()
        cls.amount = Float()
        cls.reference = String(max=80)
        cls.additionalData = String(max=100)
        cls.creationDateTime = DateTime(format="iso")
        cls.ownershipDateTime = DateTime(format="iso")

        super().__init__(**kw)

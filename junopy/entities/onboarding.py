# -*- coding: utf-8 -*-
from .lib import *


class Onboarding(JunoEntity):

    def __init__(cls, **kw):

        cls.__metadata__ = {}

        # FIELDS
        cls.type = String(max=100)
        cls.referenceId = String(max=100)
        cls.autoTransfer = Boolean()
        cls.emailOptOut = Boolean()
        cls.returnUrl = String(max=200)
        cls.refreshUrl = String(max=200)
        cls.createdOn = DateTime(format="iso")
        cls.expiresOn = DateTime(format="iso")
        cls.token = String(max=200)
        cls.url = String(max=200)

        super().__init__(**kw)

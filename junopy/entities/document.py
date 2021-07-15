# -*- coding: utf-8 -*-
from .lib import *
from junopy.entities.lib.datatype import ListType

class Document(JunoEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/documents'
		cls.__requireid__ = False
		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=100, required=True)
		cls.type = String(max=80, required=True)
		cls.description = String(max=100)
		cls.approvalStatus = String(max=80)
		cls.rejectionReason = String(max=80, required=True)
		cls.details = String(max=80, required=True)
		cls.resourceToken = String(max=80, required=True)

		super().__init__(**kw)

	def Get(self):
		if self.id:
			route = f"{self.__route__}/{self.id}"
			data = Get(route, {'resourceToken': self.resourceToken})
			self.load(**data)
			return self
		else:
			data = Get(self.__route__, {'resourceToken': self.resourceToken})
			_type = getattr(__import__('junopy.entities.document', fromlist=['Document']), 'Document')
			return ListType(_type).add([_type(**item) for item in data['_embedded']['documents']]) if '_embedded' in data else ListType(_type)

	def SendFiles(self, files:list):
		data = UploadMultiPart(f"{self.__route__}/{self.id}/files", files, {'resourceToken': self.resourceToken})
		self.load(**data)
		return self

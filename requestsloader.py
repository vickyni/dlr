# -*- coding: utf-8 -*-

import logging, os
import time

from collections import Mapping
from openpyxl import load_workbook

from function_mapping import function_mapping
from vars_setting import PARMFILE_NAME, DEF_SHEET_NAME, INVALID_VALUES

#singleton mode via decorator 
def singleton(cls):
	_instance = {}
	def _warper(*args, **kargs):
		if cls not in _instance:
			_instance[cls] = cls(*args, **kargs)
		return _instance[cls]
	return _warper

# Class definition

@singleton
class RequestsLoader(object):
	"""docstring for ParameterLoader
	load the parameter file and retrun the list of request
	"""
	def __init__(self, parameter_filename=PARMFILE_NAME, sheetname=DEF_SHEET_NAME):
		self.parameter_filename = parameter_filename
		try:
			self.wb = load_workbook(self.parameter_filename)
		except Exception as e:
			raise

		try:
			self.sheet = self.wb.get_sheet_by_name(sheetname)
		except Exception as e:
			raise

	def get_records(self):
		records = []
		for row in range(1, self.sheet.max_row+1):
			records.append(self.sheet[row])
		return records

	def get_requests(self):
		records_dict = []
		title_value = [col.value for col in self.sheet[1]]

		logging.debug('The maxrow of parameter file is %s' %self.sheet.max_row )
		
		for row in range(2, self.sheet.max_row+1):
			row_value = [ col.value for col in self.sheet[row]]
			records_dict.append(dict(zip(title_value, row_value)))
		return records_dict

	def get_functions(self, request):
		if not isinstance(request, Mapping):
			logging.error('the request type should be dict')
			raise AttributionError('the request type should be dict')

		request_func = {'logon_check':''}
		for key, val in request.items():
			if str(val).lower().strip() not in INVALID_VALUES and val is not None:
				request_func[function_mapping[key]] = val 

		request_func['run_report'] = 5
		request_func['export_report'] = ''
		return request_func
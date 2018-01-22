
from vars_setting import INVALID_VALUES
from function_mapping import function_mapping
from collections import Mapping

class ProcessAgent(object):
	"""docstring for ProcessRequest"""
	def __init__(self):
		pass
		
	def process_request(self, driver, function, value=''):
		""" 
		The function to process request via selenium server 
		drvier is the object of browserdriver which has the function to manipulate 
		action in selenium server 
		"""
		try:
			getattr(driver, function)(value)
		except Exception as e:
			driver.save_image()
			raise
			
	def makeup_functions(self, request):
		if not isinstance(request, Mapping):
			logging.error('the request type should be dict')
			raise AttributionError('the request type should be dict')

		functions = {}

		functions['logon_check'] = ''
		
		for key, val in request.items():
			if str(val).lower().strip() not in INVALID_VALUES and val is not None:
				functions[function_mapping[key]] = val 

		functions['run_report'] = 5
		functions['export_report'] = ''

		return functions
# -*- coding: utf-8 -*-

import logging, os
import time

from getpass import getpass

from browerdriver import BrowerDriver
from requestsloader import RequestsLoader

# Global Vars
from vars_setting import PARMFILE_NAME, DEF_SHEET_NAME, \
						 USERNAME, PASSWORD, INVALID_VALUES, BASE_URL

#HOSTNAME = '9.112.57.52'
HOSTNAME = '127.0.0.1'
PORT = 4444

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    #filename='app.log',
                    filemode='w'
	)

def process_request(driver, function, value=''):
	try:
		getattr(driver, function)(value)
	except Exception as e:
		raise

# Main function 

def main():
	# load parameter file 
	try:
		loadrequest = RequestsLoader(PARMFILE_NAME)
	except FileNotFoundError as e:
		logging.error(e)
	except Exception as e:
		logging.error(e)

	requests = loadrequest.get_requests()

	for request in requests:
		request_functions = loadrequest.get_functions(request)

		for key in request:
			logging.debug('%s : %s'%(key ,request[key]))

		with BrowerDriver(host=HOSTNAME,port=PORT,remote=True) as driver:
			for func, value in request_functions.items():

				try:
					process_request(driver, func, value)
				except Exception as e:
					raise

if __name__ == '__main__':
	main()
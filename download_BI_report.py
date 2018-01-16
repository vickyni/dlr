# -*- coding: utf-8 -*-

import logging, os
import time

from getpass import getpass

from browerdriver import BrowerDriver
from requestsloader import RequestsLoader

# Global Vars
from vars_setting import PARMFILE_NAME, DEF_SHEET_NAME, \
						 USERNAME, PASSWORD, BASE_URL, \
						 IS_REMOTE, IS_USER_NEEDED, \
						 HOSTNAME, PORT

if USERNAME == '' and IS_USER_NEEDED:
	from user_setting import USERNAME, PASSWORD

HOSTNAME = '9.112.57.52'
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

def download_report(parameter_file=PARMFILE_NAME, host=HOSTNAME, port=PORT, is_remote=IS_REMOTE, \
					username=USERNAME, password=PASSWORD, url=BASE_URL):
	# init the request object from excel parameter file
	try:
		logging.debug('load parameter file')
		loadrequest = RequestsLoader(parameter_file)
	except FileNotFoundError as e:
		logging.error(e)
		raise
	except Exception as e:
		logging.error(e)
		raise

	# get the requests from the request objects, type is list
	# the single request is a dict
	logging.debug('get request reocrds')
	requests = loadrequest.get_requests()

	# for each of request in the parameter file:
	for request in requests:
		# generate the selenium functions for the request, the funcion
		# is to be executed in selenium server
		request_functions = loadrequest.get_functions(request)

		# 
		with BrowerDriver(host=host, port=port, is_remote=is_remote, \
					username=username, password=password, url=url) as driver:

			for func, value in request_functions.items():
				try:
					process_request(driver, func, value)
				except Exception as e:
					raise

if __name__ == '__main__':
	download_report()
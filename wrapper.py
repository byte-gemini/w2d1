#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import json

import requests


class API:

	def __init__(self):
		self.shared_endpoint = "http://dev.markitondemand.com/MODApis/Api/vs"
		self.lookup_endpoint = self.shared_endpoint+"/Lookup/json?input="
		self.quote_endpoint = self.shared_endpoint+"/Quote/json?symbol="

	def __enter__(self):
		print('Entered __enter__')
		return self

	def __exit__(self,x,y,z):
		print('Entered __exit__')
		return self

	def lookup(self,company_name):
		response = json.loads(request.get(lookup_endpoint+company_name).text)[0]['Symbol']
		if len(respone) < 1:
			#state: no ticker symbol found for company name
			pass
		elif len(respone) > 1:
			#state: ticker symbols found for company name,
			#		but our program doesn't know which one to choose.
			pass #TODO
		else:
			#state: everything is a-okay
			return response[0]['Symbol']


	def quote(self,ticker_symbol):
		response = json.loads(request.get(quote_endpoint+ticker_symbol).text)[0]['Symbol']
		return response['LastPrice']



if __name__ == '__main__':
	from pprint import pprint
	with API() as a:
		pprint(a.quote('aapl'))
		pprint(a.quote(lookup('apple')))

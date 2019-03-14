#!/usr/bin/env python3

import json

import requests

class API:

    def __init__(self):
        self.shared_endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2'
        self.lookup_endpoint = self.shared_endpoint+'/Lookup/json?input='
        self.quote_endpoint =  self.shared_endpoint+'/Quote/json?symbol='


    def lookup(company_name): # TODO Define the args
        response =  json.loads(requests.get(lookup_endpoint+company_name).text)
        if len(response) <1:
            #State: no ticker symbol found ofr this company name
        elif len(response) >1:
            #State: multiple ticker symbols were found for this company name,
            #but our program doesn't know which one to choose.
            pass #TODO
        else:
            #State: everything's goin hunky dory
            return response[0]['Symbol']
    def quote():
        response = json.loads(requests.get(quote_endpoint+ticker_symbol).text) 

if __name__ == '__main__':
    from pprint import pprint
    pprint(lookup('tesla'))

    pprint(quote('aapl'))
    pprint(quote(lookup('apple)))

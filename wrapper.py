#!/usr/bin/env python3

import json

import requests


class API:

    def __init__(self):
        self.shared_endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2'

    def __enter__(self):
        return self

    def __exit__(self,type_,value,traceback):
        pass # TODO
        ####
        try:
            f = file.open()
        except IOError:
            pass # TODO

    def lookup(self,company_name):
        self.lookup_endpoint = self.shared_endpoint+'/Lookup/json?input='
        response = json.loads(requests.get(self.lookup_endpoint+company_name).text)
        if len(response) < 1:
            # State: no ticker symbol found for this company name
            pass # TODO
        elif len(response) > 1:
            # State: ticker symbols were found for this company name,
            #        but our program doesn't know which one to choose.
            pass # TODO
        else:
            # State: everything's going hunky-dorry
            return response[0]['Symbol']

    def quote(self,ticker_symbol):
        self.quote_endpoint  = self.shared_endpoint+'/Quote/json?symbol='
        response = json.loads(requests.get(self.quote_endpoint+ticker_symbol).text) # TODO This is kind-of repetitive
        return response['LastPrice']


if __name__ == '__main__':
    from pprint import pprint
    print('Entered the program')
    with API() as a:
        print('Entered the with statement')
        pprint(a.lookup('nvidia'))
        print('__exit__ is about to fire')
        pprint(a.quote('aapl'))
    print('__exit__ just fired')

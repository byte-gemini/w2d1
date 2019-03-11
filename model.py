#!/usr/bin/env python3

import sqlite3 #Standard library module(i.e., part of Python programming language)

import wrapper #other computers
import mapper  #local modules (i.e., this is code we're writing)

#TODO Put database stuff in 'mapper.py', later

class Database:

        # FIXME Write the constructor for the 'Database' class
	def __init__(self):
		self.connection = sqlite3.connect('master.db',check_same_thread=False)
		self.cursor = self.connection.cursor()
	def __enter__(self):
		return self

	def __exit__(self,type_,value,traceback):
		if self.connection:
			if self.cursor:
				self.connection.commit() #Basically, saving changes made to any tables
				cursor.close() #Closing the cursor object
			self.connection.close() #Closing the connection to db
	def example(self):
		pass

class User:
	def __init__(self,database_pathname):
		with Database() as db:
			db.example()

if __name__ == '__main__':
	print('I am outside of the with statement')
	with Database() as db:
		print('I am inside of the with statement')
		db.cursor.execute('DROP TABLE IF EXISTS users;')
		db.cursor.execute(
			'''CREATE TABLE users(
				pk INTEGER PRIMARY KEY AUTOINCREMENT,
				username VARCHAR,
				password VARCHAR,
				forename VARCHAR,
				surname VARCHAR
			);'''
		)
	print('I am outside the with statement again')

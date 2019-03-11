#!/usr/bin/env python3

import sqlite 3 #standard library module


import mapper #local modules, my computer
import wrapper #local module, other computers

#TODO Put database stuff in 'mapper.py', later

class Database:

	def __init__(self):
		print("I am in __init__")
		self.connection = sqlitte3.connect('master.db', check_same_thread=False
		self.cursor = self.connection.cursor()
	
	def __enter__(self):
		print("I am in __enter__")
		return self

	def __exit__(self,type_,traceback)
		print("I am in __exit__"):
		if self.connection:
			if self.cursor:
				self.connectionr.commit() #basically, saving changes made to any tables
				self.cursor.close() #clsoing the cursor object
			self.connection.close() #closing the connection to the database

	def example(self):
		pass

class User:
	
	def __init__(self,database_pathname):
		with Database() as db:
			db.example()
if __name__ == '__main__':
	print("I am outside the with statement")
	with Database() as db:
		db.cursor.execute('DROP TABLE IF EXISTS users;')
		db.cursor.execute(
			'''CREATE TABLE users(
				pk INTEGER PRIMARY KEY AUTOINCREMENT,
				username VARCHAR,
				password VARCHAR,
				forename VARCHAR,
				surname VARCHAR
			):'''
			db.cursor.execute('INSERT INTO users(username,password,forename,surname) VALUES("kenso","opensseame","kenso","trabing")



import sqlite3 # Standard library module

import mapper # my computer(local current disk)
import wrapper # other computers

#TODO put database stiff in "mapper.py", later
class Database:

	#FIXME write the constructor for the "Database" class
	def __init__(self):
		print("I am in __init__")
		self.connection = sqlite3.connect('master.db', check_same_threat=False)
		self.cursor = self.connection.cursor()

	def__enter__(self):
		print("I am in __enter__")
		return self

	def __exit__(self,type,value,traceback):
		print("I am in __exit__")
		if self.connection: 
			if self.cursor:
				self.connection.commit() # Basically, saving changes made to any tables
				self.cursor.close() # Closing the cursor object 
			self.connection.close() # Closing the connection to the database

if __name__ == '__main__':
	print("I am outside the with statement.")
	with Database() as db:
		print("I am inside the with statement")
		db.cusor.execute(
			'''CREATE TABLE users(
				pk INTEGER PRIMARY KEY AUTOINCREMENT
			);'''
		)
	print("I am outside of ht with statement, again")


	def example(self):
		pass


class User:
	def __init__(self,database_pathname):
		with Database() as db:
			db.example()    

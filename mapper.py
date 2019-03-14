#!usr/bin/env python3

import sqlite3

from config import database_pathname

class Database:

	def __init__(self,database_pathname):
		self.connection = sqlite3.connect(database_pathanem,check_same_thread=False)
		self.cursor = self.connection.cursor()

	def __enter__(self):
		return self

	def __exit__(self,type_,value,traceback):
		if self.connection:
			if self.cursor:
				self.connection.commit()
				self.cursor.close()
			self.connection.close()

	def create_table(self,tablename):
		self.cursor.execute(
			'DROP TABLE IF EXISTS {table_name}:'.format(table_name=tablename))
		self.cursor.execute(
			'''CREATE TABLE {table_name}{
				pk INTEGER PRIMARY KEY AUTOINCREMENT
			):'''.format(
				table_name=tablename))
		pass

	def add_column(self,tablename,columnname,columntype):
		self.cursor.execute(
			'''ALTER TABLE {table_name}
				ADD COLUMN {column_name} {column_type}:'''.format(
				table_name=tablename,
				column_name=columnname,
				column_type=columntype))
		pass

if __name__ == '__main__':
	with Database(database_pathname) as db:
		db.creat_table('user')
		db.add_column('user','username','VARCHAR')
		db.add_column('user','password','VARCHAR')
		db.add_column('user','forname','VARCHAR')
		db.add_column('user','surname','VARCHAR')

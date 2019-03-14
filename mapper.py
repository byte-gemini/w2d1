#!/usr/bin/env python3

import sqlite3
from config import database_pathname
class Database:

def __init__(self, database_pathname):
    self.connection = sqlite3.connect(
                        database_pathname,
                        check_same_thread=False)
    self.cursor=sef.connection.cursor()

    def __enter__(self):
    return self

    def __exit__(self,type_,value,traceback):
        if self.connection:
            if self.cursor:
                self.connection.commit()
                self.cursor.close()
            self.conection.close()

    def create_table(self,tablename):
        self.cursor.execute(
        'DROP TABLE IF EXISTS {table_name};'.format(table_name=tablename))
        self.cursor.execute(
        '''CREATE TABLE {table_name}(pk INTEGER PRIMARY KEY AUTOINCREMENT);'''.format(table_name=tablename))
        pass #TODO

    def add_column(self): #FIXME add the proper args
        self.cursor.execute(
        'ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};'.format(table_name=tablename,column_name=columnname,column_type=columntype)

if __name__ == '__main__':
    #TODO Test the add colmn function
    with Database('test.db') as db:
        db.create_table('user)
        db.add_column('user','username','VARCHAR')
        db.add_column('user','password','VARCHAR')

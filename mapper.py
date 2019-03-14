#!/usr/bin/env python3

import sqlite3

from config import database_pathname


class Database:

    def __init__(self,database_pathname):
        self.connection = sqlite3.connect(
                            database_pathname,
                            check_same_thread=False)
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
            'DROP TABLE IF EXISTS {table_name};'.format(
                table_name=tablename))
        self.cursor.execute(
            '''CREATE TABLE {table_name}(
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );'''.format(
                table_name=tablename))
        pass # TODO Return the last row id (of DBMS)

    def add_column(self,tablename,columnname,columntype):
        self.cursor.execute(
            '''ALTER TABLE {table_name}
                ADD COLUMN {column_name} {column_type};'''.format(
                table_name=tablename,
                column_name=columnname,
                column_type=columntype))
        pass # TODO Return the last row id (of DBMS)


if __name__ == '__main__':
    # TODO Test the add_column function, in tandem with the create_table function
    with Database(database_pathname) as db:
        db.create_table('users')
        db.add_column('users','username','VARCHAR')
        db.add_column('users','password','VARCHAR')
        db.add_column('users','forename','VARCHAR')
        db.add_column('users','surname','VARCHAR')

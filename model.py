#!/usr/bin/env python3

import sqlite3

import mapper
import wrapper


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('master.db',check_same_thread=False)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self,type_,value,traceback):
        if self.connection:
            if self.cursor:
                self.connection.commit() # Basically, saving changes made to any tables
                self.cursor.close() # Closing the cursor object
            self.connection.close() # Closing the connection to the database


if __name__ == '__main__':
    with Database() as db:
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
        db.cursor.execute('INSERT INTO users(username,password,forename,surname) VALUES("kenso","opensesame","kenso","trabing");')

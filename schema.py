#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('test.db',check_same_thread=False)
cursor = connection.cursor()


create_statement = 'CREATE TABLE users(pk INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR);'
cursor.execute(create_statement)


cursor.close()
connection.close()

#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('test.db',check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    '''INSERT INTO users(
        username
    ) VALUES(
        'kenso'
    );'''
)

connection.commit()
cursor.close()
connection.close()

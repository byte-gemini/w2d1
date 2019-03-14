#!/usr/bin/env python3

import sqlite3 #Standard library module(i.e., part of Python programming language)
import da
import wrapper #other computers
import mapper  #local modules (i.e., this is code we're writing)

#TODO Put database stuff in 'mapper.py', later

class Portfolio:
    pass #

#Something like a transaction log,
#but it's limited to the user's interaction
class Ledger:
    pass #a

class User:
	def __init__(self,database_pathname):
		with Database() as db:
			db.example()
    def __enter__(self):
        return self

    def __exit__(self,type_,value,tracebook):
        pass

    def authenticate(self,password):
        with Database('master.db') as db:
            db.cursor.execute(
                    'SELECT password FROM users WHERE username="{username}";'.format(username=self.usename)


            password = db.cursor.fetchone()
            return password

    def login(self,password):
        with Database(database_pathname) as db:
             db.cursor.execute('SELECT password FROM users WHERE username="{username}";
                                '.format(username=self.username))
             password = db.cursor.fetchone()
             if len(password)<1:
                 #user not found
                 return False
            elif len(password) >1:
                 return False
            else:
                 return True
  
    def signup(self,password,forename, surname):
        with Database(database_pathname) as db:
           # TODO check if username is taken
            db.cursor.execute('''INSERT INTO users (username, password, forename, surname) VALUES
                              ({username},{password},{forename},{surname});'''.format(
                              username = self.username, password = self.password,forename = self.forename,
                               surname = self.surname)) 
            temp_= True
            if temp_:
                return True
            else:
                return False

if __name__ ==  '__main__':
    with User('1337af') as u:
        u.signup('opensesame','kenso','trabing')

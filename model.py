#!/usr/bin/env python3

from config import database_pathname
from mapper import Database


class Portfolio:
    pass # TODO

class Ledger:
    pass # TODO

class User:

    def __init__(self,username):
        self.username = username

    def __enter__(self):
        return self

    def __exit__(self,type_,value,traceback):
        pass # TODO

    def login(self,password):
        with Database(database_pathname) as db:
            db.cursor.execute(
                'SELECT password FROM users WHERE username="{username}";'.format(
                username=self.username))
            password =  db.cursor.fetchall()
            if len(password) < 1:
                # State: user not found
                return False
            elif len(password) > 1:
                # State: username is not unique
                return False
            else:
                return True


    def signup(self,password,forename,surname):
        with Database(database_pathname) as db:
            db.cursor.execute(
                'SELECT username FROM users WHERE username="{username}";'.format(
                username=self.username))
            username = db.cursor.fetchall()
            if len(username) < 1:
                db.cursor.execute(
                    '''INSERT INTO users(
                        username,password,forename,surname
                        ) VALUES("{username}","{password}","{forename}","{surname}"
                    );'''.format(
                        username=self.username,
                        password=password,
                        forename=forename,
                        surname=surname))
                # pass # TODO Return last row id
                return 'works'
            else:
                pass # TODO Return last row id

if __name__ == '__main__':
    with User('1337af') as u:
        u.signup('opensesame','kenso','trabing')
    with User('420blazin') as u:
        u.signup('opensesame','tony','park')
    with User('360noscope') as u:
        u.signup('opensesame','leroy','jenkins')
    with User('illfuckyouuppp') as u:
        u.signup('opensesame','jacob','lucas')

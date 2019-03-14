#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from mapper import Database

from config import database_pathname

class Portfolio:
	pass #TODO

# Something like a transaction log,
# but its limited to the users interaaction

class Ledger:
	pass #TODO

class User:

	def __init__(self,username):
		self.username = username

	def __enter__(self):
		return self

	def __exit__(self,type_,value,traceback):
		pass #TODO

	def authenticate(self,password):
		with Database(database_pathname) as db:
			db.cursor.execute(
				'SELECT password FROM users WHERE username="{username}";'.format(username=self.username
				)
				password = db.cursor.fetchall()
				return password

	def login(self,password):
		with Database(database_pathname) as db:
			db.cursor.execute(
				'SELECT password FROM users WHERE username="{username}":'.format(
				username=self.username))
			x = db.cursor.fetchall()
			if len(password) < 1:
				#State: user not found
				return False
			elif len(password) > 1:
				#State: username not unique
				return False
			else:
				return True

	def signup(self,username,password,forename,surname):
		with Database(database_pathname) as db:
			# TODO check if username taken
			db.cursor.execute(
					'''INSERT INTO users(
						username,password,forename,surname
						) VALUES("{username}","{password}","{forname}","{surname}"
					);'''.format(
						username=self.username
						password=password
						forname=forname
						surname=surname))
			temp_ = True
			if temp_:
				return True
			else:
				return False


if __name__ == '__main__':
	with User('1337af') as u:
		u.signup('opensesame','y','z')
	with User('420blazin') as u:
		u.signup('opensesame','tony','park')
	with User('360noscope') as u:
		u.signup('opensesame','leroy','jenkins')
	with User('illfuckyouup') as u:
		u.signup('opensesame','jacob','lucas')

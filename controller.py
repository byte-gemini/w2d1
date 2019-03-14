#!/usr/bin.env python 3

from model import User

import wrapper

def game_loop():
	user_input = view.main_menu()
	acceptable_inputs = ['login',
						'signup',
						'deposit',
						'withdrawl']
	while True:
		if user_input in acceptable_inputs:
			if user_input == 'login':
				(username,password) = view.login_menu()
				with User(username) as u:
					if u.login(password):
						a = view.dashboard()
						return a
			elif user_input == 'signup':
				(username,password,forename,surname) = view.signup_menu()
				with User(username) as u:
					a = u.signup(password,forename,surname)
					user_choice = view.dashboard()
					return a
			elif user_input == 'deposit':
				x = view.deposit_menu()
				#TODO return
			elif user_input == 'withdrawl':
				x = view.withdrawl_menu()
				#TODO return
			else:
				return 'bad inputs 2'
		else:
			return 'bad inputs'


if __name__ =='__main__':
	game_loop()

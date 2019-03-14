#1/usr/bin/env python3

import model
import view

# TODO Flesh out this sub method.

def game_loop():

	user_input = view.main_menu()
	acceptable_inputs = ['login','signup','deposit','withdrawl']
	
	while True:
	    if user_input in acceptable_inputs:
	        if user_input == 'login':
	            (username,password) = view.login_menu()
            
                with User('kenso') as u:
                    z = u.login(password)
                    a = view.dashboard() #calls view 
	                return a
	        ###
	        elif user_input == 'signup':
	            (username,password,forename,surname) = view.signup_menu()
	            with User('username') as u:
	                a= u.signup(password,forename,surname)) #this passes these values
	                                                        # to the users class
	                return a 
	                ###
	        elif user_input == 'deposit':
	            x = view.deposit.menu()
	        
	        elif usesr_input == 'withdrawl'
	            x = view.withdrawl_menu()
	        
	        else:
	 else:
	        return 'bad inputs'
	        
if __name__ == '__main__':
    print(game_loop()	

#!/usr/bin/env python3

from model import User
import view


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
                        return a # TODO
                    else:
                        pass
                ###
                ### FIXME FIXME FIXME FIXME FIXME FIXME
                ###
            elif user_input == 'signup':
                (username,password,forename,surname) = view.signup_menu()
                with User(username) as u:
                    a = u.signup('toor','websi','nebsi')
                    return a # TODO
                # return # TODO
                ###
                ###
                ###
            elif user_input == 'deposit':


                x = view.deposit_menu()
                # return # TODO
            elif user_input == 'withdrawl':
                x = view.withdrawl_menu()
                # return # TODO
            else:
                # State: Bad credentials,
                #        and it isn't being caught
                #        in the parent condition.
                return 'bad inputs 2'
        else:
            # State: Bad credentials
            return 'bad inputs'


if __name__ == '__main__':
    print(game_loop())

#!/usr/bin/env python3

import os


def header():
    os.system('clear')
    os.system('cowsay -d "Welcome to Zombie Academy"')

def main_menu():
    header()
    return input('What do you want to do? ')

def login_menu():
    header()
    return input('Username: '),input('Password: ')

def signup_menu():
    header()
    pass # FIXME

def dashboard():
    header()
    print('[d] Deposit\n[w] Withdraw\n[c] Check Balance\n')
    return input('What do you want to do? ')

def deposit_menu():
    header()
    pass # TODO


def withdrawl_menu():
    header()
    pass # TODO


if __name__ == '__main__':
    main_menu()

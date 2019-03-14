#!/usr/bin/env python3
import os

def header():
    os.system('clear')
    os.system('cowsay -d "welcome to zombie academy"')

def main_menu():
    header()
    return input ('whats up')

def login_menu():
    return input('username: '),input('password')

def signup_menu():
    return input('username: '),input('password'),input('forename'),input('surname')

def dashboard():  #this called by controller
    print('[d] Deposit \n  [w] withdraw\n [c] check balance')
    
def deposit_menu():
    pass
    
 

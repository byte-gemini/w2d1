def header():
	os.system('clear')
	os.system('cowsay -d "Welcome to Zombie Academy")

def main_menu():
	header()
	return input('What do you want to do?')

def dashboard():
	header()
	print('[d] Deposit\n[w] Withdraw\n[c] Check Balance')
	return input('What do you want to do? ')

def login_menu():
	header()
	return input('Username: '), input('Password: '), input('Forename: '), input('Surname: ')

def signup_menu():
	return input('Username: '), input('Password: '), input('Forename: '), input('Surname: ')

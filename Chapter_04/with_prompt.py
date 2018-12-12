import getpass
try:
	p = getpass.getpass("Enter your password: ")
except Exception as error:
	print('ERROR', error)
else:
	print('Password entered:', p)


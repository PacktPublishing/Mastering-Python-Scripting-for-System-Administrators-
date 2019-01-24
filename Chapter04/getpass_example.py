import getpass
passwd = getpass.getpass(prompt='Enter your password: ')
if passwd.lower() == '#pythonworld':
	print('Welcome!!')
else:
	print('The password entered is incorrect!!')


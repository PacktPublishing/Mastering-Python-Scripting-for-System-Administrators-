import getpass
user_name = getpass.getuser()
print ("User Name : %s" % user_name)
while True:
	passwd = getpass.getpass("Enter your Password : ")
 	if passwd == '#pythonworld':
		print ("Welcome!!!")
		break
	else:
		print ("The password you entered is incorrect.")


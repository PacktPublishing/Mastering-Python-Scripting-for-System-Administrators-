from ftplib import FTP

ftp = FTP('192.168.2.105')
ftp.login('student','training')

ftp.cwd('/home/student/work/')
files = ftp.nlst()

# Print out the files
for file in files:
	print("Downloading..." + file)
	ftp.retrbinary("RETR " + file ,open("/home/student/testing/" + file, 'wb').write)

ftp.close()


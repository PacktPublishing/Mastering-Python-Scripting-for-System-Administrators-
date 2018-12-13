from ftplib import FTP

ftp = FTP('192.168.2.105')
ftp.login('student','training')

welcome_msg = ftp.getwelcome()
print(welcome_msg)

ftp.close()


from ftplib import FTP

ftp = FTP('192.168.2.105')
ftp.login('student','training')

ftp.cwd('/home/student/')
s_cmd_stat = ftp.sendcmd('STAT')
print(s_cmd_stat)
print()
s_cmd_pwd = ftp.sendcmd('PWD')
print(s_cmd_pwd)
print()

ftp.close()


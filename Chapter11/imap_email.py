import imaplib
import pprint

imap_server = 'imap.gmail.com'
username = 'Emaild_address'
password = getpass.getpass()

imap_obj = imaplib.IMAP4_SSL(imap_server)
imap_obj.login(username, password)
imap_obj.select('Inbox')
temp, data_obj = imap_obj.search(None, 'ALL')
for data in data_obj[0].split():
	temp, data_obj = imap_obj.fetch(data, '(RFC822)')
	print('Message: {0}\n'.format(data))
	pprint.pprint(data_obj[0][1])
	break
imap_obj.close()


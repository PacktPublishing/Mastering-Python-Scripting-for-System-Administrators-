import poplib

pop3_server = 'pop.gmail.com'
username = 'Emaild_address'
password = getpass.getpass()

email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)
print("\nLatest Mail\n")
latest_email = email_obj.retr(1)
print(latest_email[1])


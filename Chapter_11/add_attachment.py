import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass

host_name = 'smtp.gmail.com'
port = 465

sender = 'mansi.joshi990@gmail.com'
password = getpass.getpass()
receiver = 'kalpesh7402patil@gmail.com'

text = MIMEMultipart()
text['Subject'] = 'Test Attachment'
text['From'] = sender
text['To'] = receiver

txt = MIMEText('Sending a sample image.')
text.attach(txt)

f_path = '/home/student/Desktop/mountain.jpg'
with open(f_path, 'rb') as f:
	img = MIMEImage(f.read())

img.add_header('Content-Disposition',
               'attachment',
               filename=os.path.basename(f_path))
text.attach(img)

s = smtplib.SMTP_SSL(host_name, port)
print("Attachment sent successfully !!")
s.login(sender, password)
s.sendmail(sender, receiver, text.as_string())
s.quit()

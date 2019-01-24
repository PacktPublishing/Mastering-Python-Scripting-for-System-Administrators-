import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass

host_name = 'smtp.gmail.com'  # smtp.mail.yahoo.com
port = 465
u_name = 'mansi.joshi990@gmail.com'
password = getpass.getpass()
sender = 'Mansi Joshi'
receivers = ['info@levanatech.com', 'kalpesh7402patil@gmail.com']

text = MIMEMultipart()
text['Subject'] = 'Test Attachment'
text['From'] = sender
text['To'] = ', '.join(receivers)

txt = MIMEText('Sending a sample image.')
text.attach(txt)

f_path = '/home/student/Desktop/mountain.jpg'
with open(f_path, 'rb') as f:
    img = MIMEImage(f.read())

img.add_header('Content-Disposition',
               'attachment',
               filename=os.path.basename(f_path))
text.attach(img)

server = smtplib.SMTP_SSL(host_name, port)
print("Attachment sent successfully !!")
server.login(u_name, password)
server.sendmail(sender, receivers, text.as_string())
server.quit()

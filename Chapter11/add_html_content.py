import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

host_name = 'smtp.gmail.com'
port = 465

sender = 'mansi.joshi990@gmail.com'
password = getpass.getpass()
receiver = 'kalpesh7402patil@gmail.com'

text = MIMEMultipart()
text['Subject'] = 'Test HTML Content'
text['From'] = sender
text['To'] = receiver

msg = """\
<html>
  <body>
    <p>Hello there, <br>
       Good day !!<br>
       <a href="http://www.imdb.com">Home</a> 
    </p>
  </body>
</html>
"""
html_content = MIMEText(msg, "html")
text.attach(html_content)

s = smtplib.SMTP_SSL(host_name, port)
print("Attachment sent successfully !!")
s.login(sender, password)
s.sendmail(sender, receiver, text.as_string())
s.quit()

#!/usr/local/bin/python
#email program which sends two attachments, 1. Plain format 2. HTML format
#src:http://stackoverflow.com/questions/882712/sending-html-email-using-python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'mahalesainath@gmail.com'
receiver ='mahalesainath@gmail.com'

# creating a message container
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = sender
msg['To'] = receiver

#creation of the body of message - 1. Plain format 2. HTML format
text = "Hi\nI am speaking with you from plain_text version of the body!\n Carpe Diem"
html ="""\
<html>
<head></head>
<body>
<p>hi<br>
how are you ? <br>
this is a link <b> <a href="http://www.python.org">the link </a> </b> you were looking for.
</p>
</body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

#attach parts into message container
msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('localhost')

s.sendmail(sender,receiver,msg.as_string())
s.quit()

import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPException 

fp = open('textfile.txt', 'rb')

msg = MIMEText(fp.read())

fp.close()

msg['Subject'] = 'The contents of %s' % msg
msg['From'] = 'Your email'
msg['To'] = 'receiver email address'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('Your email', 'Your password')
try:
    server.sendmail('Your email', ['receiver email address'], msg.as_string())        
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"

server.quit()

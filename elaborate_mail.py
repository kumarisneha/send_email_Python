import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = 'Your email'
toaddr = 'Receiver email'
msg = MIMEMultipart()
msg['From'] = 'Your email'
msg['To'] = 'Receiver email'
msg['Subject'] = "Sendind mail through python script"
 
body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('Your email', "your password")
text = msg.as_string()
try:
    server.sendmail(fromaddr,toaddr , text)        
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"

server.quit()


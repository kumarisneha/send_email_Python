import smtplib
from smtplib import SMTPException  
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login( "YOUR EMAIL", "YOUR PASSWORD")
 
msg = "Write your message. "

try:
    server.sendmail("YOUR EMAIL", "ADDRESS YOU WANT TO SEND TO", msg)        
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"

server.quit()



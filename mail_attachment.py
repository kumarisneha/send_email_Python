import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "YOUR EMAIL"
toaddr = 'RECEIVER EMAIL'
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Resume"
 
body = "In this mail i attached my resume"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = 'textfile.txt'
attachment = open(filename, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR PASSWORD")
text = msg.as_string()
try:
    server.sendmail(fromaddr,toaddr , text)        
    print "Successfully sent email"
except SMTPException:
    print "Error: unable to send email"

server.quit()

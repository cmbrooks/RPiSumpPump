import smtplib

fromaddr = 'codymb36@gmail.com'
toaddrs = 'codymb36@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'codymb36'
password = '$inspire26.8*'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
from datetime import datetime

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
floatSwitch = GPIO.input(17)

import smtplib

running = True
now = datetime.now()
log = open("sumpPumpLog.txt", "r+")
startTime = now.time()


def elapsedTime():
    """This function checks how much time
    has elapsed since the timer has started"""
    currentTime = now.time()
    return startTime - currentTime


def sendEmail(*msg):
    """This function sends an email to selected recipients with a custom
    message as well as the log file attached."""
    #enter the code that sends an email to the family with the log attached

    fromaddr = 'codymb36@gmail.com'
    toaddrs = 'codymb36@gmail.com'
    msg = """The sump pump has been deemed not working.
    Please see the Pi and the data log file for more details."""

    # Credentials (if needed)
    username = 'codymb36'
    password = '$inspire26.8*'

    msg.attached()

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


while running is True:
    if floatSwitch is True:
        #Write the time and what happened to the file
        log.write(str(now) + "Float switch turned on")
        #Wait until switch is turned off
        while floatSwitch is True:
            #Add start time elapsed
            startTime = now.time()
            if floatSwitch is False:
                log.write(str(now) + "Float switch turned off")
                break
            #if elapsedTime > 3 min
            elif elapsedTime() > 3:
                log.write(str(now) + "Sump Pump has been deemed broaken")
                sendEmail("The sump pump is now broken.")



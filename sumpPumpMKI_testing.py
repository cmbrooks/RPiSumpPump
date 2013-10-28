print ("The Script has started")

import time
from datetime import datetime
now = datetime.time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

import smtplib

running = True
log = open("/media/RPIDATA/sumpPumpLog.txt", "r+")
starttime = time.time()


def floatSwitch():
    return GPIO.input(17)


def elapsedTime():
    """This function checks how much time
    has elapsed since the timer has started"""
    endtime = time.time()
    elapsed = endtime - starttime
    return elapsed


def sendEmail(msg):
    """This function sends an email to selected recipients with a custom
    message as well as the log file attached."""
    #enter the code that sends an email to the family with the log attached

    fromaddr = 'brookssumppump@gmail.com'
    toaddrs = ['codymb36@gmail.com']
    finalmsg = msg + """Please see the Pi and the data
log file for more details."""

    # Credentials (if needed)
    username = 'brookssumppump'
    password = '!sumppump*'

    finalmsg.attached()

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


while running is True:
    if floatSwitch() is 0:
        #Write the time and what happened to the file
        log.write(str(now) + " Float switch turned on")
        print "The float switch turned on"
        #Wait until switch is turned off

        while floatSwitch() == 0:
            startTime = time.time()
            if floatSwitch() is 1:
                log.write(str(now) + " Float switch turned off")
                print "Float switch turned off"
                break
            #if elapsedTime > 3 min (in the form of 180 seconds)
            elif elapsedTime() > 180:
                log.write(str(now) + " Sump Pump has been deemed broaken")
                print ("Sump Pump is broken")
                sendEmail("The sump pump is now broken.")
                print ("An email has been sent saying the sump pump is broken.")
                break

            time.sleep(0.05)

log.write(str(now) + " The sctipt has stopped.")
print ("The script has stopped")
log.close

sendEmail("The script has stopped.")
print ("An email was sent sayig 'The script has stopped'")
log.close

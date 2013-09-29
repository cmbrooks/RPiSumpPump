import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
floatSwitch = GPIO.input(17)

import smtplib

running = True
log = open("sumpPumpLog.txt", "r+")
startTime = time.time()


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

    fromaddr = 'from@email.com'
    toaddrs = ['to@email.com']
    finalmsg = msg + """Please see the Pi and the data log file for more details."""

    # Credentials (if needed)
    username = 'my_username'
    password = 'my_password'

    finalmsg.attached()

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


if running is True:
    if floatSwitch is True:
        #Write the time and what happened to the file
        log.write(str(time.time() + "Float switch turned on"))
        #Wait until switch is turned off

        while floatSwitch:
            startTime = time.time()
            if floatSwitch is False:
                log.write(str(now) + "Float switch turned off")
                break
            #if elapsedTime > 3 min (in the form of 180 seconds)
            elif elapsedTime() > 180:
                log.write(str(now) + "Sump Pump has been deemed broaken")
                sendEmail("The sump pump is now broken.")

else:
    log.write(str(time.time() + "The sctipt has stopped.")
    sendEmail("The script has been stopped.")
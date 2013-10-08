import time

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)
#floatSwitch = GPIO.input(17)

floatSwitch = True

import smtplib

running = True
log = open("H:\Documents\Code\PythonCode\SumpPump\sumpPumpLog.txt", "r+")
starttime = time.time()


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


def story():
    print """Once upon a time, there was a sump pump. The sump pump was in a
family's basement. The family depended on the sump pump for their saftey.
one night, there was a storm. The sump was broken though, and the basement
flooded without the family knowing. This is a sad story. If only I was
there to save the family's basement. The end."""


while running is True:
    user_input = raw_input("What would you like to do?")

    if user_input == "Tell me a story":
        story()
    elif user_input == "What is your name":
        print """I do not have a name. I am only a computer that has no soul.
    My sole purpose is to protect your sump pump and your basement. I will
    give my life to protect it. My dying words will be contained in an email
    that says, 'Your sump pump is now broken.'"""
    elif user_input == "stop":
        break
    else:
        print "I do not recognize that command. Please try agian."

    if floatSwitch is True:
        #Write the time and what happened to the file
        log.write(str(time.time() + "Float switch turned on"))
        #Wait until switch is turned off

        while floatSwitch:
            startTime = time.time()
            if floatSwitch is False:
                log.write(str(time.time()) + "Float switch turned off")
                break
            #if elapsedTime > 3 min (in the form of 180 seconds)
            elif elapsedTime() > 180:
                log.write(str(time.time() + "Sump Pump has been deemed broaken"))
                sendEmail("The sump pump is now broken.")
                break

log.write(str(time.time() + "The sctipt has stopped."))
sendEmail("The script has stopped.")

print ("The Script has started")

import time
from datetime import datetime
now = datetime.time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
floatSwitch = GPIO.input(17)

import smtplib

running = True
log = open("/media/RPIDATA/sumpPumpLog.txt", "r+")
starttime = time.time()


def elapsedTime():
    """This function checks how much time
    has elapsed since the timer has started"""
    endtime = time.time()
    elapsed = endtime - starttime
    return elapsed


while running == True:
    if floatSwitch == 1:
        print "The switch turned on"
        running = False
    else:
        running = True

print "I'm done now,"
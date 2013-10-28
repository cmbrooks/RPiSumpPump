print ("The script has started")

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)


def floatSwitch():
    return GPIO.input(17)


log = open("/media/RPIDATA/sumpPumpLog.txt", "r+")

while True:
    log.write("\n" + str(floatSwitch()))
    print floatSwitch()
    time.sleep(3)
    if floatSwitch == 1:
        break
log.close
print ("The script has started")

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
floatSwitch = GPIO.input(17)

log = open("/media/RPIDATA/sumpPumpLog.txt", "r+")

log.write("\n" + str(floatSwitch))
print (str(floatSwitch))
log.close

print ("The script has started")

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
floatSwitch = GPIO.input(17)

print (str(floatSwitch))

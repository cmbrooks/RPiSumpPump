import time
from datetime import datetime


def now():
    return datetime.now()

starttime = now


def elapsedTime(function):
    """This function checks how much time
    has elapsed since the timer has started"""

    if function == "start":
        endtime = time.time()
    elif function == "pause":
        endtime = starttime
    elif function == "print":
        print (endtime - float(starttime))

    elapsed = (endtime - starttime)
    return elapsed

while True:
    elapsedTime(raw_input("what now?"))
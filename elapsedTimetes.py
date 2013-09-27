from datetime import datetime
now = datetime.now()


def elapsedTime():
    """This function checks how much time
    has elapsed since the timer has started"""
    currentTime = now.time()
    elapsed = str(startTime) - str(currentTime
    return elapsed


startTime = now.time()
while True:
    print (elapsedTime())


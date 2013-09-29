import time

starttime = time.time()

while True:
    raw_input("Please Press any button to show the time elapsed")
    currenttime = time.time()
    elapsedtime = currenttime - starttime
    print elapsedtime
    break
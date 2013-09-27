from datetime import datetime

now = datetime.now()
startTime = datetime.now()
elapsedTime = datetime.now() - startTime
while True:
    print now
    if raw_input("Press enter when ready to print time elapsed"):
        break
    else:

print elapsedTime
print now
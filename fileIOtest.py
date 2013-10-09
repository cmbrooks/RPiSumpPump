from datetime import datetime
now = datetime.now

log = open("/home/cody/Documents/Code/PythonCode/SumpPump/sumpPumpLog.txt", "r+")
printed = log.write(str(now()) + " Hello World")
print (printed)
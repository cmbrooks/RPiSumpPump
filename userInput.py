running = True
floatSwitch = False
log = open("C:\Users\cobrooks\Documents\RPiSumpPump-testing\RPiSumpPump-testing\sumpPumpLog.txt", "r+")

def story():
    print """Once upon a time, there was a sump pump. The sump pump was in a
family's basement. The family depended on the sump pump for their saftey.
one night, there was a storm. The sump was broken though, and the basement
flooded without the family knowing. This is a sad story. If only I was
there to save the family's basement. \n The end."""


def name():
     print """I do not have a name. I am only a computer that has no
soul. My sole purpose is to protect your sump pump and your basement. I will
give my life to protect it. My dying words will be contained in an email
that says, 'Your sump pump is now broken.' \n"""


while running is True:

    user_input = raw_input("What would you like to do? \n").lower()

    if user_input == "Tell me a story":
        story()
    elif user_input == "What is your name":
        name()
    elif user_input == "status":
        if floatSwitch == True:
            print "The switch is up"
        else:
            print "The switch is down"
    elif user_input == "history":
        print log.readline(-2)
        print log.readline(-1) + "\n"
    elif user_input == "exit" or "stop":
        break
    else:
        print "I do not recognize that command. Please try agian."
print "Have a nice day!"
import datetime 
now = datetime.datetime.now()
print(now.hour)
myvar = input("what is the current hour in military time 0-23?")
if myvar == ("0 1 2 3 4 "):
    print ("Its early. You should be sleeping!")
if myvar == ("5 6"):
    print ("Wake up, brew that coffee, get that mile run in, and get that breakfast…")
if myvar == ("7 8 "):
    print ("Time to go to work.")
if myvar == ("9 10 11"):
    print ("You should be working!")
if myvar == ("12"):
    print ("Take your lunch break")
if myvar == ("13 14 15 16"):
    print ("Do you feel that afternoon lull?")
if myvar == ("17 18"):
    print ("Time to hit the gym")
if myvar == ("19 20"):
    print ("gotta eat that dinner")
if myvar == ("21 22 23"):
    print ("Get that sleep and repeat")
else:
    print ("You didn’t type an acceptable value! (0-23)")
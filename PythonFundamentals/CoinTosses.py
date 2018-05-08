#write a function that stimulates tossing a coin 5,000 times
#your function should print how many times the head/tail appears

#use python built-in round function to conver floating number into integer  -  round()

import random

#reps = number of tosses + 1

def coinToss(reps):
    print "Starting the program..."
    headCount = 0
    tailCount = 0
    for x in range(1, reps):
        toss = round(random.random())
        if toss == 0:
            headCount += 1
            print "Attempt #", x, ": Throwing a coin...it's a head! So far we have", headCount, "head(s) and", tailCount, "tail(s)!"
        else:
            tailCount += 1
            print "Attempt #", x, ": Throwing a coin...it's a tail! So far we have", headCount, "head(s) and", tailCount, "tail(s)!"
    print "Ending the program. Goodbye!"


coinToss(11)



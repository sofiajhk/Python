#write a function that generates 10 scores between 60-100
#for each score, your function should dispaly what the grade is (A, B, C, D)

#use random.randint(a,b) to generate random numbers 
#this will return a random integer N such that a <= N <= b

import random #to get access to random module, you must add import random to top of program

def grades(repeat):
    print "Scores and Grades"
    for x in range(0, repeat):
        grade = random.randint(60, 100)
        if 60 <= grade <= 69:
            print "Score:", grade,"; Grade: D"
        elif 70 <= grade <= 79:
            print "Score:", grade,"; Grade: C"
        elif 80 <= grade <= 89:
            print "Score:", grade,"; Grade: B"
        elif 90 <= grade <= 100:
            print "Score:", grade,"; Grade: A"
        else:
            print "Sorry...you failed!"
    print "That's all folks!"

grades(10)
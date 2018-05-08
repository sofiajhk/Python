#multiples part 1: write code that prints all odd numbers from 1-1000 using a for loop
#range([start], stop[, step])
for count in range(1, 1001, 2): #to index 1001 because 1000 will not include the value 1000
    print count

#multipes part 2: write another code that prints all multiples of 5 from 5-1,000,000
for count in range(5, 1000001, 5):
    print count

#create a program that prints the sum of all the values in the list
a = [1, 2, 5, 10, 255, 3]
sum = 0 #create a variable for sum first
for i in a:
    sum += i
print "sum:", sum #different indentation bc if not, it will loop and show sum after each number, not TOTAL sum

#create a program that prints the average of the values in the list
print "average:", sum/len(a)
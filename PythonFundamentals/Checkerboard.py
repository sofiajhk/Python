#write a program that prints a "checkerboard" pattern to the console
#you should not require an input (use looping)
#output should look like this...
#* * * *
# * * * *
#* * * *
# * * * * etc.

for count in range(0, 10):
    if count%2 == 0: #if it is an even number
        print '* ' * 4 #make sure space is AFTER *
    else:
        print ' *' * 4 #make sure space is BEFORE *

        
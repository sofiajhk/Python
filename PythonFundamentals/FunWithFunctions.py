#create a function that counts 1-2000 and print each number and specify odd/even

def odd_even():
    for count in range(1, 2001):
        if count%2 == 0:
            print "Number:", count, "even!" #don't forget commas after/before quotes or else error!
        else:
            print "Number:", count, "odd!"

odd_even()



#create a funtion that iterates through each value in list and returns a list where each value has been multiplied by 5

before_list = [1, 71, -13, 0, 42]

def multiply(list, multiple):
    after_list = []
    for i in range(0, len(list)):
        list[i] *= multiple
        after_list.append(list[i])
    print after_list

multiply(before_list, 5)

#OR use "return" attribute so you don't need to create a separate list...

def multiply2(list, multiple):
    for i in range(0, len(list)):
        list[i] *= multiple
    return list

print multiply2(before_list, 5)



#write a function that takes the multiply function call as an argument.
#your function should return the multiplied list as a 2-dimensional list
#each internal list should contain the 1's times the number in the orginal list

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0, x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array
    print new_array

print layered_multiples(multiply([1, 3, 6], 5))

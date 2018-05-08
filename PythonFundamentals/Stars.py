#Part 1: write a function that takes a list of numbers and prints out *

num = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(list):
    for i in list:
        print "*" * i

#draw_stars(num)

#Part 2: modify the above function to take into account both integers and strings
#when string is passed, display the first letter of the string instead of *

numInt = [4, "Sofia", 1, "Kevin", 5, 18, "Egg and Potato"]

def draw_stars2(list):
    for i in list:
        if type(i) is int:
            print "*" * i
        else:
            length = len(i)
            letter = i[0].upper()
            print letter * length

draw_stars2(numInt)

#alternate solution - from coding dojo

def stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

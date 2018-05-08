#write a program that takes a list of strings and a string containing a single character
#and prints a new list of all the strings containing that character

before_list = ['woah', 'i', 'can', 'dance', 'yo']
sing_str = "o"

def find_letter(list, character):
    after_list = [] #create an empty list to store results
    for i in range(0, len(list)):
        if list[i].find(character) == 1: #find the letter for every index of list and if it contains 'o', it will == 1 (true)
            after_list.append(list[i])
    print after_list

find_letter(before_list, sing_str)
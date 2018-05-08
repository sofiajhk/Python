#write a function that takes in a dictionary and returns a list of tuples 
#where the first tuple item is the key and second is the value

myDict = {
    "first book": "Harry Potter and the Sorcerer's Stone",
    "second book": "Harry Potter and the Chamber of Secrets",
    "third book": "Harry Potter and the Prisoner of Azkaban",
    "fourth book": "Harry Potter and the Goblet of Fire",
    "fifth book": "Harry Potter and the Order of the Pheonix",
    "sixth book": "Harry Potter and the Half-Blood Prince",
    "seventh book": "Harry Potter and the Deathly Hallows"
}

def makeTup(dict):
    tupList = zip(dict.keys(), dict.values())
    print tupList
    return tupList

makeTup(myDict)

#ALTERNATE SOLUTION: from Coding Dojo

def making_tupes(the_dict):
    the_list = []
    # here, k and v will parse each tuple of key,value pairs returned by .iteritems()
    for k, v in the_dict.iteritems():
        the_list.append((k,v))
    print the_list
    return the_list

making_tupes(myDict)
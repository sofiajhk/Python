#create a function that takes in two lists and creates a single dictionary
#first list contains keys, second list contains values (assume the lengths are the same)

name = ["Poppy", "Creek", "Bridget", "Branch", "Biggie", "King Peppy", "Girstle"]
hair_color = ["pink", "sea foam", "rainbow", "black", "aqua", "gray-red", "green"]


def makeDict(list1, list2):
    newTup = zip(list1, list2)
    newDict = dict(newTup)
    print newDict
    return newDict

makeDict(name, hair_color)

#ALTERNATE SOLUTION: from Coding Dojo

def makeDict2(list1, list2):
    newDict = {}
    for i in range(0, len(list1)):
        newDict[list1[i]] = list2[i]
    print newDict
    return newDict

makeDict2(name, hair_color)
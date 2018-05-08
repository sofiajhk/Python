#create a dictionary containing info about yourself (keys should include name, age, country of birth, favorite language, etc)
#write a function that will print something like...
#My name is ...
#My age is ... 
#My country of birth is ...
#My favorite language is ...

#dict.items() returns a LIST of 2-tuples ([(key, value), (key, value), ...])
#dict.iteritems() is a generator that yields 2-tuples.

#str(): Return a string containing a nicely printable representation of an object

aboutSofia = {"name": "Sofia", "age": "24", "country of birth": "South Korea", "favorite language": "Python"}

def aboutMe(dict):
    for key, value in dict.iteritems():
        print "My", key, "is", str(value), "."

aboutMe(aboutSofia)

#OR
#concatenating variables to strings commonly done with the .format() method 
#(can be used on any string, or variable that contains a string)

def aboutMe2(dict):
    for key, value in dict.iteritems():
        print "My {} is {}.".format(key, value)

aboutMe2(aboutSofia)
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#write a program that, given some value, tests the value for its type
#integer: greater than or equal to 100, print "that's a big number!" / less than 100, print "that's a small number!"
#string: greater than or equal to 50 characters, print "long sentence!" / shorter than 50 characters, print "short sentence!"
#list" length is greater than or equal to 10, print "BIG LIST!" / fewer than 10 values, print "short list!"

#create a variable for the value you are testing
test_var = aL

#check for type
test_type = type(test_var)
print test_type
if test_type is int:
    if test_var >= 100:
        print "that's a big nummber!"
    else:
        print "that's a small number!"
elif test_type is str:
    if len(test_var) >= 50:
        print "long sentence1"
    else:
        print "short sentence!"
elif isinstance(test_var, list):  #isinstance(object, classinfo) tests if object is classinfo/type
    if len(test_var) >= 10:
        print "BIG LIST!"
    else:
        print "short list!"
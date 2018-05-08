students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#given the list above, create a program that outputs just the names (First Last)

def cohort(list):
    for name in list:
        print name['first_name'], name['last_name']

#cohort(students)



users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

#given the dictionary above, create a program that prints in the following format
#Students
#1 - MICHAEL JORDAN - 13 ETC.
#Instructors
#1 - MICHAEL CHOI - 11 ETC.

def cohortAll(dict):
    for position in dict:
        print position
        count = 0
        for person in dict[position]:
            count += 1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(first_name) + len(last_name)
            print "#{} - {} {} - {}".format(count, first_name, last_name, length)
    
cohortAll(users)
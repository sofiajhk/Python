# You're creating a program for a call center. Every time a call comes in you need a way to track that call. 
# One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter
from datetime import datetime

class Call(object):
    #number of people on call list starts at 0
    counter = 0
    def __init__(self, name, phone_num, reason):
        self.id = Call.counter
        # id = their placement on the call list
        self.name = name
        self.phone_num = phone_num
        self.time = datetime.now()
        self.reason = reason

        # adds a caller everytime someone calls/every time there is an instance
        Call.counter += 1
    def display(self):
        print "ID: {} \nName: {} \nNumber: {} \nTime: {} \nReason: {} \n".format(self.id, self.name, self.phone_num, self.time, self.reason)
        # the "\n prints the value on a new line"
        return self

# CallCenter class should have attributes...
# calls: list of call objects 
# queue: length of calls in queue/length of call list
# Call Center class should have methods...
# add: adds a new call to the end of the queue/call list
# remove: removes the call from beginning of list (index 0)
# info: prints name and phone # for each call in queue and length of queue

# if everything is working, add a method that can find and remove from the queue 
# by finding the phone #

class CallCenter(object):
    def __init__(self):
        # create an empty list for call objects/instance of Call class
        self.calls = []
        self.queue = 0
    def add(self, call):
        self.calls.append(call)
        self.queue += 1
        return self
    def remove(self):
        # removing call from call list at index 0
        self.calls.pop(0)
        self.queue -= 1
        return self
    def remove_number(self, number):
        for caller in self.calls:
            if number == caller.phone_num:
                self.calls.pop(self.calls.index(caller))
                self.queue -= 1
        return self
    def info(self):
        print self.calls
        for info in self.calls:
            # calling upon the display method from Call class
            print info.display()
        print self.queue


call1 = Call("Kevin", 3124567889, "help")
call2 = Call("Maria", 7732145563, "financial")
call3 = Call("Mina", 8789065422, "other")
call4 = Call("Sara", 2731552632, "bill")
call5 = Call("Brian", 3561120000, "service")

# call1.display()
# call2.display()
# call3.display()
# call4.display()
# call5.display()

center = CallCenter()
center.add(call1).add(call2).add(call3).add(call4).add(call5).remove().remove_number(8789065422).info()
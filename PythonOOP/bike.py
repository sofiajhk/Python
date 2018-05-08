# create a new class called Bike with the following properties/attributes: price, max_speed, miles 
# initial miles is set to 0 whenever a new instance is created
class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    # create displayInfo() function and have this method display bike's price, maximum spped, and total miles
    def displayInfo(self):
        print "This bikes costs $", self.price,"."
        print "The max speed for this bike is ", self.max_speed,"MPH."
        print "This bike has been riden for", self.miles, "miles."
    # create ride() function and have it display "Riding" on the screen and increase the total miles ridden by 10
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    # create reverse() function and have it display "Reversing" on the screen and decrease the total miles ridden by 5
    def reverse(self):
        print "Reversing"
        if self.miles <= 5:
            self.miles = 0
        else:
            self.miles -= 5
        return self
        
# "return self" statement allows you to chain methods, instead of running functions/methods individually

# create 3 instances of the Bike class
# first instance ride three times, reverse once and have it displayInfo()
bike1 = Bike(156,50)
bike1.ride().ride().ride().reverse().displayInfo()
# this is how you chain methods (refer to "return self" note above) 

# second instance ride twice, reverse twice and have it displayInfo()
bike2 = Bike(211,75)
bike2.ride().ride().reverse().reverse().displayInfo()

# third instance reverse three times and displayInfo().
bike3 = Bike(75, 45)
bike3.reverse().reverse().reverse().displayInfo()
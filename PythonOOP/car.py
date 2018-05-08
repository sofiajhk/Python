# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: 
# price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. 
# Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. 
# In the class have a method called display_all() that returns all the information about the car as a string. 
# In your __init__(), call this display_all() method to display information 
# about the car once the attributes have been defined.

class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 15
        else:
            self.tax = 12
        self.display_all()
    def display_all(self):
        print "Price: $",self.price
        print "Speed:", self.speed,"MPH"
        print "Fuel:", self.fuel 
        print "Mileage:", self.mileage,"MPG"
        print "Tax:", self.tax,"%"

# six instances of class Car
car1 = Car(21900,150,"Empty",20)
car2 = Car(9000,100,"Empty",17)
car3 = Car(49999,200,"Full",40)
car4 = Car(24500,135,"Empty",30)
car5 = Car(5500,90,"Full",20)
car6 = Car(10000,85,"Full",23)
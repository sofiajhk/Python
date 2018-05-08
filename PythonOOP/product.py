# create class Product that tracks product information (price, item name, weight, brand, status)
# create methods...
# sell: change status to sold
# tax: takes tax a decimal amount as parameter and returns price of item including tax
# return: takes reason for return as parameter and changes status accordingly
#   -if reason = defective, change status to defective and price to 0
#   -if returned in box, change status to "for sale"
#   -if item has been used, change status to "used" and apply 20% discount to price
# display info: show all product details

# every method that doesn't have a return statement, should "return self" so methods can be chained

class Product(object):
    def __init__(self,item_name,price,weight,brand):
        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell_item(self):
        self.status = "Sold"
        return self
    def tax_item(self, tax):
        self.tax = tax
        self.price *= (1+self.tax)
        return self
    def return_item(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = "0"
        elif reason == "used":
            self.status = "Used"
            self.price = ((self.price/(1+self.tax))*.8)
        else:
            self.price /= (1+self.tax)
            self.status = "For Sale"
        return self
    def display_all(self):
        print "Item:", self.item_name
        print "Price: $", self.price
        print "Weight:", self.weight,"LB"
        print "Brand:", self.brand
        print "Status:", self.status
        return self

phone = Product("iPhoneX",999,1.5,"Apple")
gameconsole = Product("Nintendo DS",675,4,"Nintendo")
tv = Product("30in Flatscreen Tv",750,22,"Samsung")

phone.tax_item(.11).sell_item().display_all()
gameconsole.tax_item(.15).sell_item().return_item("defective").display_all()
tv.tax_item(.11).sell_item().return_item("used").display_all()
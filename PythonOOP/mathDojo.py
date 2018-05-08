# create a class MathDojo that takes at least one integer(s) and/or list(s) 
# and/or tuple(s) of numbers as a parameter 
# then create a new instance md that can take in arguments/parameters like...
# md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
# and return something like...
# 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result

# use "return self" so you can chain methods!

class MathDojo(object):
    def __init__(self):
        self.answer = 0
    def add(self, *args):
        for value in args:
            if type(value) == list or type(value) == tuple:
                for num in value:
                    self.answer += num
            else:
                self.answer += value
        return self
    def subtract(self, *args):
        total = 0
        for value in args:
            if type(value) == list or type(value) == tuple:
                for num in value:
                    total += num
            else:
                total += value
        self.answer -= total
        return self
    def result(self):
        print self.answer

md = MathDojo()
md.add([1], 3, 4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()


# encapsulation
# acces modifier 1. public , private, protected
# if the funtion contain _ like _calling  is protected used in herited and connected class
#  # if the funtion contain __ like __calling  is private only used in same class   
# name mangling of private class _ + className + methodname
# python has weak encapsulation // python has no encapsulation 

class A:
    def init(self):
        print("init A")

    def _calling(self):
        print("calling protected")

    def __texting(self):
        print("texting private")

class B(A):
    def __init__(self):
        print("init B")



obj = B()
obj._calling()
# obj.__texting() #give error attribut not find
obj._A__texting() # using name mangling # working 


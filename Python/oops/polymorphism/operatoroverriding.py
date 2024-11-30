# operator overloading 

class Student():
    def __init__(self,marks):
        self.marks = marks

    # def __add__(self, obj2):
    #     return self.marks + obj2.marks

    def __add__(self, num):
        return self.marks + num
    
    # def __sub__(self , obj2):
    #     return self.marks - obj2.marks 

    def __sub__(self , num1, num2):
          self += num1
          
        
    def __mul__(self , obj2):
        return self.marks * obj2.marks
        
s1 = Student(100)
# s2 = Student(70)

# print(s1 + 10)
# print(s1 - s2)
# print(s1 * s2)

print(s1 - 20 )
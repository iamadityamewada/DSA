class Student:
    def __init__(self,college, name, age):
        # print("by default init")
        self.college = college
        self.name = name
        self.age = age

    # def detail(self ,name, age, height):
    #     self.name = name
    #     self.age = age
    #     self.height = height
    #     print("Detail Added")

    def show_detail(self):
        print("name:" + self.name, "age:" ,  self.age)

student = Student("LNCT", "Aditya", 21)
print(student.age,  student.name, student.college)
student.show_detail()
# student.detail("Aditya", "21", "5F")
# print(student.name)

# student.show_detail()

# // function that call imediately when object of class is created 

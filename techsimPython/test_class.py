class Student:
    def detail(self ,name, age, height):
        self.name = name
        self.age = age
        self.height = height
        print("Detail Added")

    def show_detail(self):
        print("name:" + self.name, "age:" + self.age,  "height:" + self.height) 

student = Student()
student.detail("Aditya", "21", "5F")
# print(student.name)

student.show_detail()
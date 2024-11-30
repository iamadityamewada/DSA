# user define function 
# take nothing,return nothing
# take something
# return something 

# def greet():
#     print("Good Morning")
# greet()

# def sayHello(name):
#     print(f"Hello {name}")
# sayHello("Priya")    


# def get_greet():
#     return "Good Morning"
# print(get_greet())


# factorial

# def factorial(num):
#     num = int(num)
#     if num == 0 or 1:
#         print(num)
#     else:
#         fact = 1
#         for i in range(1,num+1):
#             fact = fact*i
#         print(fact)
# factorial(6)    
# 

# def calc(num1, num2,opp):
#     if opp == "+":
#         return num1 + num2
#     elif opp == "-":
#         return num1 - num2
#     elif opp == "*":
#         return num1 * num2
#     elif opp == "/" and num2!=0:
#         return num1 / num2
#     elif opp == "//" and num2 !=0:
#         return num1 // num2
#     else:
#         return("not valid input")
        
# print(calc(0,3,"/"))

# n number of arguments
# def Add(*a):
#     # print(type(a))
#     return sum(a)
# print(Add(5,3,7,5))

# keyword args

# def stu_detail(**detail):
#     print(detail)

# stu_detail(name="Priya", gmail ="r@g.com",age ="6")

# # default argument
# def def_fun(x,y,z=10):
#     return x+y+z
# print(def_fun(4,3))


# def show_employee(name,salary=15000):
#     print(f"your name is {name} and your salary is {salary}")
# show_employee("Priya")
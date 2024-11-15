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

def calc(num1, num2,opp):
    if opp == "+":
        return num1 + num2
    elif opp == "-":
        return num1 - num2
    elif opp == "*":
        return num1 * num2
    elif opp == "/" and num2!=0:
        return num1 / num2
    elif opp == "//" and num2 !=0:
        return num1 // num2
    else:
        return("not valid input")
        
print(calc(0,3,"/"))
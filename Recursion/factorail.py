num = int(input("No: "))


def factorial(num):
    if num == 1:
        return num
    
    return num*factorial(num-1)

print("factorial: ",factorial(num))
# when function call itself until to get desire output
# it has to part base case and recursive case

#example 


def factorial(num):
    if num <= 0:
        return None
    elif num == 1 or num == 0:
        return 1
    
    return num * factorial(num -1)

print(factorial(5))


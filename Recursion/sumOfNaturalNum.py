def sumOfN(num:int):
    if num <= 0:
        return 1
    
    return num + sumOfN(num - 1)

print(sumOfN(5))
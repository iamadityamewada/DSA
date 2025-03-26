num = int(input("Enter No. : "))

def sum_n(num):
    if num == 1:
        return num
    
    return num + sum_n(num-1)

print("sum is : ", sum_n(num))
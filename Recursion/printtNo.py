
# num =  int(input("Enter the number: "))

# def print_number(start,num):
#     if start == num:
#         print(num)
#         return
#     print(start)
#     print_number(start+1,num)

# print_number(0,num)  





num =  int(input("Enter the number: "))

def print_rev_number(num):
    if num == 0:
        print(num)
        return
    print(num)
    print_rev_number(num - 1)

print_rev_number(num)


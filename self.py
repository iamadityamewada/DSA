# input = "HelloAdityaYouAreCool"
# output = ["Hello", "Aditya","You","Are","Cool"]

#msg = input("Enter a Msg: ")
# msg = "HelloAdityaYouAreCool"
# word =""
# res=[]
# for i in msg:
#     if i==i.upper() and word!="":
#         res.append(word)
#         word=""
#     word = word + i
# res.append(word)    
# print(res)
    
def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Input from the user
number = int(input("Enter a number to check if it's a power of 3: "))

# Check and output the result
if is_power_of_three(number):
    print(f"{number} is a power of 3.")
else:
    print(f"{number} is not a power of 3.")

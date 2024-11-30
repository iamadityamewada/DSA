ls = [10,20,30,40,50]

# print(ls[:3])

# print(ls[-2:])

# print(ls[-2:])

# my_string = "PythonProgramming"
# print(my_string[2:5]) #tho

# ls = [1,2,3,4,5,6]

# print(ls[::2])

# ls = ["a","b","c","d","e"]
# print(ls[:4])

# ls = [1,2,3,4,5,6]
# print(ls[::-1])

# ls=[100,200,300,400,500]
# print(ls[1:])

# my_str = "abcdef"
# print(my_str[::2])

# ls = [10,20,30,40,50,60]
# print(ls[1:-1])

# ls = [1,2,3,4,5,6]
# print(ls[3:3])

# ls = [1,2,3,4,5,6]
# ls1 = ls[0:]

# print(id(ls), ls)
# print(id(ls1), ls1)


# my_str = "python"
# print([my_str[::-1]])

# number check 
# num = int(input("enter no: "))
# if(num>0):
#     print("postive")
# elif(num==0):
#     print("num is zero")
# else:
#     print("nagative")       

#even odd 
# num = int(input("enter no: "))
# if(num%2==0):
#     print("even")
# else:
#     print("odd")

#
# num = int(input("enter no: "))
# num = int(input("enter no: "))
# if(num>=18):
#     print("adult")
# else:
#     print("not adult")

# grade = input("grade:")
# grade = grade.upper()

# match(grade):
#     case("A"):
#         print("Exellent")
#     case("B"):
#         print("Good")
#     case("C"):
#         print("Average")
#     case("D"):
#         print("Below Average")
#     case("F"):
#         print("Fail")   
#     case _:
#         print("invalid grade")     


# num = int(input(""))
# digit_count = 0
# while True:
#     if num//10 != 0:
#         num //=10
#         digit_count +=1
#     elif num//10==0:
#         digit_count +=1
#         break   
# if(digit_count==1):
#     print("single Digit")
# elif(digit_count == 2):
#     print("Dounble Digit")
# else:
#     print("multiple Digit")     
# print(digit_count)       
# 


s ="Python is cool and sorted"
# print(s.split())


# def split_method(s):
#     ls = []
#     wd = ""
#     for word in s:
#         if word!=" " :
#             wd = wd + word
#         elif(word == " "):
#             ls.append(wd)
#             wd = ""
#     ls.append(wd)
#     return ls  
  
# print(split_method(s))        
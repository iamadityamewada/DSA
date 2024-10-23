#.........................01.........................
# date = input("Enter a Date:")
# date = date.split("-")
# date = [date[1],date[2],date[0]]
# date = "-".join(date)
# print(date)

#..........................02...........................
#input "John Adam Smith"
# Output: "JAS"
# name = input("Enter a msg: ")
# name = name.split(" ")
# name = name[0][0] + name[1][0] + name[2][0]
# print(name)

#......................03........................
# msg = "Dear [name] your appointement is confirmed for [date]"
# name = input("enter name: ")
# date = input("enter date: ")
# msg = msg.replace('[name]',name)
# msg = msg.replace('[date]', date)
# print(msg)

# .........................04........................
# msg = input("Enter msg: ")
# print(msg == msg[::-1])

#..........................05........................

# grocery_list = ["milk","bread","eggs","butter","cheese"]
# print(grocery_list)
# grocery_list.append("fruits")
# print(grocery_list)
# grocery_list.insert(3,"vegetable")
# print(grocery_list)
# grocery_list.remove("bread")
# print(grocery_list)
# print("index of cheese: ",grocery_list.index("cheese"))
# grocery_list.sort()
# print(grocery_list)

#........................................06....................................
# attendance_list = ["Aarav","Isha","Rohan","Ananya","Kabir"]
# attendance_list.append("Neha")
# attendance_list.remove("Aarav")
# attendance_list.sort()
# print(len(attendance_list))
# print(attendance_list)
# attendance_list.clear()
# print(attendance_list)

# monthly_expense = [10,2,3,5,10]
# print(monthly_expense)
# monthly_expense.append(500)
# print(monthly_expense)
# monthly_expense.insert(1,100)
# print(monthly_expense)
# monthly_expense.remove(3)
# print(monthly_expense)
# print(max(monthly_expense))
# print(min(monthly_expense))
# print(sum(monthly_expense))

#...........................................07.............................................................
# li = [3,6,7,3,4,5,34]
# postion = int(input("enter positon: "))
# num = int(input("enter num: "))
# li.insert(postion,num)
# print(li)
#...........................................08.............................................................

# age = int(input("Enter your age: "))

# if age>=18:
#     print("You are eligible for driving license")

# ........................................09....................................................................

# temp = int(input("enter temp: "))

# if temp>30:
#     print("koi ac chala do yaar")
# elif temp<10:
#     print("bhai heater chala do thandi lag rahi hai")
# else:
#     print("koi dikkat nahi sab mast hai") 
# 

#...........................................10................................................................

# age = int(input("enter the age: "))

# if age<12:
#     print("the prize is 150")
# elif age >= 60:
#     print("the prize is 200")
# else:
#     print("the prize is 300")  
# 
# ...........................................11..............................................................
# no = int(input("enter number"))
# if no % 2 == 0:
#     print("even")
# else:
#     print("odd")    

#..............................................12...............................................................

# day = input("enter the day: ")
# workday = ["monday", "tuesday", "wednesday","thursday","friday"]
# if day.lower()=="saturday" or day.lower()=="sunday":
#     print("you can relax")
# elif day.lower() in workday:
#     print("its working day")
# else:
#     print("you enter the wrong day")   
# 
# ...........................................................13...........................................................
# # 

# fruits = ["apple","banana","cherry","mango"]
# # find banana in list and print banana is found
# for _ in fruits:
#     if _.lower() == "banana":
#         print("banana is found")

#.........................................................14...................................................................

# names = ["John", "Alice","BoB","Zara"]
# for x in names:
#     if x[0].lower() == "a":
#         print(x)

#.......................................................15......................................................................

# words = ["apple","banana","cherry","mango"]

# for x in words:
#     if len(x) > 5:
#         print(x)

#........................................................16...........................................................................

# numbers = [-4,-5,-9,-4,-56,-32,4,5,3]

# for num in numbers:
#     if num<0:
#       print("nagative number found")          
#     break
# else:
#    print("no nagative number")
#............................................................17...................................................................

# av = 5

# order = int(input("enter count of candy: "))

# for i in range(0,av):
#         print("candy")
#         if i == order-1:
#               break         
# else:
#    print("out of stock")

#/.............................................................18..................................................................



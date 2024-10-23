# start = int(input("Enter starting point:- "))
# end = int(input("Enter end point:- "))
# op=range(start,end+1)
# print(list(op))

# s = int(input("enter start tablie:-"))
# b = range(s,s*11,s)
# print(list(b))

# li = range(1,11)
# for i in li:
#     print(i)

# li = [1,2,3,4,53,21,34]
# for i in li:
#     print("Hello")

# li=("hello")
# for i in li:
#     print(i)

# li=[12,34,56,44,56]
# for i in li:
#     print(i)

# li=[12,34,56,44,56]
# for i in li:
#     print(i+5)

# for i in range(1,11):
#     print (i)

# student={
#     "name": "mahak",
#     "college" : "lnct",
#     "age": 21
# }

# for i in student:
#     print(student[i])


# for i in range(50,101):
#     if i%2==0 and i%3==0:
#         print(i)

# data=("abc34yu7823qew")
# for i in data:
#     if i.isdigit():
#      print(i, "- digit")
#     elif i.isalpha():
#        print(i, "- char")

# data2=("sdggfhgjbncfgtrsdfiui")
# vowel=["a","e","i","o","u"]
# for i in data2:
#     if  i.lower() in vowel:
#       print(i,("-vowel"))
#     else:
#       print (i,("-consonent"))



# li=[45,34,54,67,23,87]
# s=0
# for i in li:
#   s=s+i
# print(s)

# li=[45,34,54,67,23,87]
# s=0
# for i in li:
#  if i%2==0:
#    s=s+i
# print(s)


# li=[2,3,4,5,6]
# new=[]
# for i in li:
#     s=i*i
#     new.append(s)
# print(new)

# msg="class will be over in 10 minutes"
# new=msg.split()
# for i in new:
#     print(i)


s="hello"
new=[]
li=list(s)
for i in s:
    last_char = li.pop()
    li.insert(0,last_char)
    ab = "".join(li)
    new.append(ab)
print(new)


s = "hello"
li = list(s)
new =[]

for s in li:
    last_char = li.pop()
    li.insert(0,last_char)
    ab = "".join(li)
    new.append(ab)
print(new)

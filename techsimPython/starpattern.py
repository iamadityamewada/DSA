
# num = 5
# for i in range(0,5):
#     print("*"*num)
#     num = num - 1


# for i in range(5,0,-1):
#     print("*"*i)

# for i in range(0,6):
#     print("*"*i)

# num = 0
# for i in range(7,0,-2):
#     print(" "*num,  "*"*i)
#     num = num + 1

# space = len(range(1,10,2))-1
# for i in range(1,10,2):
#     print(" "*space, "*"*i)
#     space-=1

#      *
#     ***
#    *****
#   *******
#  *********

# hours = [11,12,13,14]

# for h in hours:
#     for m in range(60):
#         print(f"{h}:{m}")

# colors = ['red','green','blue']
# object= ['ball',"box"]

# for c in colors:
#     for o in object:
#         print(f"{c} {o}")


# list1 = [1,2,3]
# list2 = [4,5,6]

# for li in list1:
#     for li2 in list2:
#         print(f"{li}+{li2}={li+li2}")

list1 = [1,3,4,6,7]
list2 = [2,3,5,6,8]
common = []
for num in list1:
    if(num in list2):
        common.append(num)
print(common)        
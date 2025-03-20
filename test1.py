# #  two sum 
# def two_sum():
#     target = 7
#     ls = [4,5,2,2]
#     n = 4
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if ls[i] + ls[j] == target:
#                  print(i,j)

            


# # two_sum()


# def index_of():
#       class Node:
#           def __init__(self,value):
#                self.value = value
#                self.next = None

#       class Linkedlist: 
#           def __init__(self):
#               self.head = None
#               self.tail = None

#           def append(self,value):
#               node = Node(value)
#               if self.head == None:
#                   self.head = node
#                   self.tail = node
#               else:
#                   self.tail.next = node
#                   self.tail = node        

#           def num_index(self,i):
#               temp = self.head
#               n = 0
#               while temp is not None:
#                    if n == i:
#                      print(temp.value)
#                    temp = temp.next  
#                    n +=1      
#       myls = Linkedlist()
#       myls.append(4)
#       myls.append(7)
#       myls.append(6)
#       myls.append(5)
#       myls.num_index(3)

# # index_of()      


# # # longest substring of non repeating char

# # def longest_substring():
# #     s = "abcdeafgh"
# #     sub = ""
# #     for char in s:
# #         if char not in sub:
# #             sub = sub + char
# #         else:
# #             return len(sub)

# # # print(longest_substring())


# # def anagram():
# #     s = "anagram" 
# #     t = "magram"
# #     s= list(s)
# #     t = list(t)
# #     return sorted(s) == sorted(t)

# # # print(anagram())




# # #  median of sorted array

# # def median():
# #     ls1 = [4,5,6,7]
# #     ls2 = [3,4,5,7]
# #     ls = ls1 + ls2
# #     ls.sort()
# #     l = len(ls)
# #     if l % 2 == 0:
# #         m = (ls[l//2] + ls[l//2 - 1])/2
# #         print(m)
# #     else:
# #         print(ls[(l-1)//2])

# # # median()   
# 
# 
# 

N, X = map(int, input().split())

def find_kid_position(N, X):
    return (X % N) + 1


result = find_kid_position(N, X)

print(result)
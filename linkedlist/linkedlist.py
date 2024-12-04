# node = {
#     "head":{
#         "value":11,
#         "next":{
#             "value":23,
#             "next":{
#                "value":7,
#                "next":{
#                   "value":4,
#                   "next":{
#                      "value":19,
#                      "next":None
#                          }
#                       }
#                    }
#             }
#         }
#     }
# # print(node)
# print(node["head"]["next"]["next"]["value"])


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node   
     
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node



my_linkedlist = LinkedList(11)
my_linkedlist.append(12)
my_linkedlist.append(34)
my_linkedlist.append(32)


# print(my_linkedlist.head.value)
# print(my_linkedlist.tail.value)
# print(my_linkedlist.head.next.next.next.value)
# print(my_linkedlist)   



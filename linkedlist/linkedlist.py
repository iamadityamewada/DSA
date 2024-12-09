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

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node

#     def append(self,value):
#         new_node = Node(value)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node    

# ls = LinkedList(12)
# ls.append(23)
# ls.append(24)

# print(ls.head.value)
# print(ls.tail.value)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node   

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end = "->")
            temp = temp.next                     
        print(temp)
   
    # def print_list(self):
    #     temp = self.head
    #     while temp is not None:
    #         if temp.value % 2  == 0 :
    #           print(temp.value, end = "->")
    #         temp = temp.next
                                 
    #     print(temp)

    def prepend(self,value):
        new_node = Node(value)   
        # print(new_node.value, new_node.next) 
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            # print(new_node.value, new_node.next)
            new_node.next = self.head
            self.head = new_node

    def pop_first(self):
        if self.head == None:
            return "Empty List"
        else:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value
    

ls = LinkedList()
ls.append(23)
ls.append(24)
ls.append(32)
ls.append(28)
ls.append(42)
ls.append(23)
ls.print_list()
ls.prepend(11)
ls.print_list()
print("poped item:", ls.pop_first())
ls.print_list()

# print(ls.head.value)
# print(ls.tail.value)

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
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node   
        self.length += 1

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
    def get(self,index):
        if index >= 0 and index <= self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            print(temp.value)
            return temp
        else:
            print ("index out of range")
        
    def set(self,index,val):
            temp = self.get(index)
            temp.value = val

    def insert(self, index, value):
        if index <0 or index > self.length - 1:
            print(None)
        elif index == 0:
            self.prepend(value)
        elif index == self.length - 1:
            self.append(value)    
        else:
            new_node = Node(value)
            pre_node = self.get(index - 1)
            temp = pre_node.next
            pre_node.next = new_node
            new_node.next = temp 
            self.length +=1  

    def remove(self, index):
        if index <0 or index > self.length - 1:
            print(None)
        elif index == 0:
            self.pop_first
        elif index == self.length - 1:
            self.pop() 
        else:
            pre_node = self.get(index - 1)
            pre_node.next = pre_node.next.next
            print(pre_node.next.value)

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
        self.length += 1

    def pop_first(self):
        if self.head == None:
            return "Empty List"
        else:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return value
        
    def pop(self):
        if self.head == None:
            None
        else: 
            prev = self.head
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1    
            return temp.value

# ls = LinkedList()
# ls.append(23)
# ls.append(24)
# ls.append(32)
# ls.append(28)
# ls.append(42)
# ls.append(23)
# ls.print_list()
# ls.remove(4)
# ls.print_list()



# ls = LinkedList()
# ls.append(23)
# ls.append(24)
# ls.append(32)
# ls.append(28)
# ls.append(42)
# ls.append(23)
# ls.print_list()
# ls.prepend(11)
# ls.print_list()
# print("poped item:", ls.pop_first())
# print(ls.pop(),"pop")
# ls.print_list()
# print(ls.length)
# ls.get(10)
# ls.set(2,25)
# ls.print_list()
# ls.insert(3,45)
# ls.print_list()


# print(ls.head.value)
# print(ls.tail.value)

ls = LinkedList()
ls.append(23)
ls.append(24)
ls.append(32)
ls.append(28)
ls.append(42)
ls.append(23)
ls.print_list()

ls1 = LinkedList()
ls1.append(49)
ls1.append(53)
ls1.append(78)

ls1.print_list()

temp = ls.head
while temp.next is not None:
    temp = temp.next
temp.next = ls1.head

ls.print_list()
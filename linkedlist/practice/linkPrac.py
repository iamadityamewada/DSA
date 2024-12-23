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
   
    def get(self,index):
        temp = self.head
        if index >= 0 and index < self.length:
            for _ in range(index):
                temp = temp.next
            # print(temp.value)
            return temp
        else:
            print ("index out of range")
        
    def set(self,index,val):
            temp = self.get(index)
            temp.value = val

    def insert(self, index, value):
        if index < 0 or index > self.length - 1:
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
            self.length += 1  

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

    def reverse(self):
        rev = None
        temp = self.head
        while temp != None:
            next_node = temp.next
            temp.next = rev
            rev = temp
            temp = next_node
        self.head = rev

## practice question  partition list 
    def compare(self, val):
        small = LinkedList()
        greater = LinkedList()
        temp = self.head
        while temp is not None:
            if temp.value>=val:
                greater.append(temp.value)
            else:
                small.append(temp.value)
            temp = temp.next    
        
        temp = small.head
        if temp:
            while temp.next is not None:
                temp = temp.next   
            temp.next = greater.head  
            self.head = small.head                       
        else:
            self.head = greater.head
ls = LinkedList()
ls.append(44)
ls.append(33)
ls.append(12)
ls.append(5)
ls.append(7)
ls.append(57)
# ls.print_list()
# ls.reverse()
ls.compare(33)
ls.print_list()
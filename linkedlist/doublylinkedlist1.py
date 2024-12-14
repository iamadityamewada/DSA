class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def printlist(self):
        temp = self.head
        print(None,end="<-")
        while temp is not None:
            print(temp.value,end="<->")
            temp = temp.next
        print(temp)


    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
    
    def popfirst(self):
        if self.head == None:
            print(None)
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            print(temp.value)
            self.length-=1
    def pop(self):
        if self.length == 0:
            print(None)
        else:
            temp = self.tail
            self.tail = temp.prev
            if self.length > 1:
                self.tail.next = None
            print(temp.value)
            self.length -=1
            if self.length == 0:
                self.head = None
                self.tail = None

    def getNode(self,index):
        if index >= 0 and index <= self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            # print(temp.value)
            return temp
        else:
            return None    
    
    def getValue(self,index):
        node = self.getNode(index)
        if(node):
            print(node.value)
        else:
            print("index out of range") 

    def insert(self, index, value):
        if index< 0 or index > self.length - 1:
            print(None)
        elif index == 0:
            self.prepend(value) 
        elif index == self.length:
            self.append(value)   
        else:
            new_node = Node(value)
            before = self.getNode(index-1)
            after = before.next
            new_node.next = after
            new_node.prev = before
            before.next = new_node
            after.prev = new_node
            self.length +=1


dll = DoublyLinkedList()
dll.append(12)
dll.append(13)
dll.append(19)
dll.append(20)
dll.append(19)
dll.printlist()

node = dll.getNode(4)

print("node.value: ", node.value)
dll.getValue(6)
dll.printlist()
dll.insert(2,22)
dll.printlist()

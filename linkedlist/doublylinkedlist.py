class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end="->")
    # def push(self,value):
    #     new_node = Node(value)
    #     if           

dls = DLinkedList()
print(dls.head, dls.tail, dls.length)    
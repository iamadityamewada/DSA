class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end="->")
            temp = temp.next
    
    def append(self,val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail= node
            

ls = LinkedList()
ls.append(44)
ls.append(43)
ls.append(55)
ls.append(32)
ls.append(25)

# ls.print_list()

def findMiddle(ls:LinkedList):
    temp = ls.head
    length = 0
    # count length of list
    while temp is not None:
        length +=1
        temp = temp.next
    temp = ls.head    
    for i in range(length//2):
        temp = temp.next
    return temp
node = findMiddle(ls)
print(node.val)        
            
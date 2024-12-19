class Node:
        def __init__(self,value):
            self.value = value
            self.next = None

class linkdedlist:
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
            self.length +=1

      def print_list(self):
            temp = self.head
            while temp is not None:
                  print(temp.value, end="->")
                  temp = temp.next
            print()      
      
      def prepend(self,value):
            new_node = Node(value)
            if self.head == None:
                  self.head = new_node
            else:
                  new_node.next = self.head
                  self.head = new_node 
            self.length +=1          
      
      def pop_first(self):
            if self.head is None:
                  return "empty linked list"
            else:
                  temp = self.head.value
                  self.head = self.head.next
                  if self.head == None:
                        self.head = None
                  self.length -=1
                  return temp
            
      def get(self,index):
            if index < 0 or index>=self.length:
                  print(None)   
            else:
                  temp = self.head
                  for _ in range(index):
                        temp = temp.next
                        return temp
                                  

                                    
ls = linkdedlist()
ls.append(44)
ls.append(77)
ls.append(34)
ls.prepend(14)
# ls.print_list()
# print(ls.length)
# print("first ele", ls.pop_first())
ls.print_list()
# print(ls.length)
print(ls.get(2).value)

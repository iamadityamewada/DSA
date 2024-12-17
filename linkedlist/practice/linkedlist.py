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

                                    
ls = linkdedlist()
ls.append(44)
ls.append(77)
ls.append(34)
ls.prepend(14)
ls.print_list()
print(ls.length)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(f"{item} push to stack")   

    def pop(self):
        if len(self.stack) > 0:
           last_item = self.stack.pop()
           print(last_item)
        else:
            print("stack is empty")
    
    def peek(self):
        print(self.stack[len(self.stack)-1])

    def display_stack(self):
        print("<-".join(self.stack))    


# book_stack = Stack()
# book_stack.push("Rework")
# book_stack.push("The lean startup")
# book_stack.push("atomic habbit")
# # book_stack.pop()   
# # book_stack.pop()
# # book_stack.pop()    
# # book_stack.peek()   
# book_stack.display_stack()  

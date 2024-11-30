class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(f"{item} to stack")   

    def pop(self):
        if len(self.stack) > 0:
           self.stack.pop()
        else:
            print("stack is empty")
    
                           
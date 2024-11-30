class queue:
    def __init__(self):
        self.queue = []

    def enque(self, item):
        self.queue.append(item)
        print(f"{item} is enqued")

    def deque(self):
        first_item = self.queue.pop(0)
        print(first_item)

    def front(self):
        print(self.queue[0])

    def display_queue(self):
        print("->".join(self.queue))  

q = queue()
q.enque("5")
q.enque("6") 
q.enque("7")
q.deque()
q.display_queue()
q.front()                             
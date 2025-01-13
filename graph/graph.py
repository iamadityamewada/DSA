class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        all_keys = self.nodes.keys()
        if value not in all_keys:
            new_node = Node(value)
            self.nodes[value] = new_node
            print("node created")
        else:
            print("node already created")    

graph = Graph()
graph.add_node(33)

print(graph.nodes)


                
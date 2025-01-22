class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []

class Weighted_graph:
    def __init__(self):
        self.nodes = {}

    def add_nodes(self,value):
        allnodekey = self.nodes.keys()
        if value not in allnodekey:
            new_node = Node(value)
            self.nodes[value] = new_node
            print("node added")
        else:
            print("node already exist") 

    def add_connections(self, v1, v2 , dis):
        if v1 in self.nodes.keys() and v2 in self.nodes.keys(): 
            v1 = self.nodes[v1]
            v2 = self.nodes[v2]
            v1.neighbors.append((v2, dis))
            v2.neighbors.append((v1, dis))
            print("connected")
        else:
            print("node doesnt exist")       

    def print_graph(self):
        for node in self.nodes:
            node = self.nodes[node]
            print(node.value , end = "->")
            for n,dis in node.neighbors:
                print(f"({n.value},distance : {dis})", end=",")
            print()                         

    # def total_distance(self,start):
    #     queue = []
    #     visited = []
    #     distance = []
    #     start_node = self.nodes[start]
    #     queue.append(start_node)
    #     queue.append(start_node)
    #     while len(queue)>0:
    #         node = queue.pop(0)
    #         for n and dis in node.neighbors:
    #             if n not in visited:

    def total_distance(self, start):
            node = self.nodes[start]
            distance = 0
            for n,dis in node.neighbors:
                distance = distance + dis
            return distance    

               

            

wg = Weighted_graph()
wg.add_nodes(1)
wg.add_nodes(2)
wg.add_nodes(3)
wg.add_nodes(4)
wg.add_nodes(5)
wg.add_nodes(6)
wg.add_connections(1,2,1)
wg.add_connections(2,3,1)
wg.add_connections(3,5,2)
wg.add_connections(4,2,2)
wg.print_graph()

print(wg.total_distance(2))







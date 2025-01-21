class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []
    
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self,value):
        all_keys = self.nodes.keys()
        if value not in all_keys:
            new_node = Node(value)
            self.nodes[value] = new_node
            print("node created")
        else:
            print("already node created")

    def add_connection(self,node1_value,node2_value):
        all_keys = self.nodes.keys()
        if node1_value in all_keys and node2_value in all_keys:
            node1 = self.nodes[node1_value]
            node2 = self.nodes[node2_value]
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
            print("Connected")
        else:
            print("Nodes should present in the graph")

    def print_graph(self):
        for node_name in self.nodes:
            print(node_name,end="->")
            node = self.nodes[node_name]
            connections = node.neighbors
            for n in connections:
                print(n.value,end=",")
            print()

    def remove_connection(self,value):
        if value in self.nodes.keys():
            r_node = self.nodes[value]
            for node_name in self.nodes:
                connections = self.nodes[node_name].neighbors
                if r_node in connections:
                    connections.remove(r_node)
            
            # self.nodes.pop(value)
            # remove node
            del self.nodes[value]
        else:
            print("Node not found") 

    def bfs(self):
        result = []
        visited =[]
        for node_name in self.nodes:
            queue = []
            first_node = self.nodes[node_name]
            if first_node not in visited:
                queue.append(first_node)
                visited.append(first_node)
            while len(queue)>0:
                node = queue.pop(0)
                result.append(node.value)
                for n in node.neighbors:
                    if n not in visited:
                        queue.append(n)
                        visited.append(n)
        return result                    

    def has_path(self,start,end):
        result = []
        visited = []
        queue = []
        first_node = self.nodes[start]
        if first_node not in visited:
            queue.append(first_node)
            visited.append(first_node)
            if first_node.value == end:
                result.append(n.value)
                print(result)
                return True
        while len(queue)>0:
            node = queue.pop(0)
            result.append(node.value)
            for n in node.neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.append(n)
                    if n.value == end:
                        result.append(n.value)
                        print(result)
                        return True
        return False                           
    
    def connected_node(self,node):
        res = []
        visited = []
        queue = []
        fnode = self.nodes[node]
        queue.append(fnode)
        visited.append(fnode)
        while len(queue)>0:
            node = queue.pop(0)
            res.append(node.value)
            for n in node.neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.append(n)
        return res  
    

    def find_path(self,start,end):
        res = []
        que = []
        visited = []
        start_node = self.nodes[start]
        que.append(start_node)
        visited.append(start_node)
        while len(que)>0:
            node = que.pop(0)
            res.append(node.value)
            if node.value == end:
                return res
            for nb in node.neighbors:
                if nb not in visited:
                    que.append(nb)
                    visited.append(nb)

    def find_the_largest_island(self):
        result = []
        visited =[]
        for node_name in self.nodes:
            queue = []
            first_node = self.nodes[node_name]
            if first_node not in visited:
                queue.append(first_node)
                visited.append(first_node)
                value = []
            while len(queue)>0:
                node = queue.pop(0)
                value.append(node.value)
                for n in node.neighbors:
                    if n not in visited:
                        queue.append(n)
                        visited.append(n)
            result.append(value)
        print(result)    
        return max(result, key=len) 
                            



            




my_graph = Graph()
print(my_graph.nodes)
my_graph.add_node("A")
my_graph.add_node("B")
my_graph.add_node("E")
my_graph.add_node("D")
my_graph.add_node("F")
my_graph.add_connection('A',"B")
my_graph.add_connection("B","D")
my_graph.add_connection("D","E")
my_graph.print_graph()
# print(my_graph.bfs())
# print(my_graph.has_path("B","E"))
# print(my_graph.connected_node("A"))
# print(my_graph.find_path("A","E"))
print(my_graph.find_the_largest_island())


                
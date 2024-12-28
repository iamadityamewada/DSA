class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
       self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node  
        else:      
            temp = self.root
            while True:
                if new_node.value < temp.value:
                    if temp.left == None:
                        temp.left = new_node
                        return True 
                    temp = temp.left
                elif new_node.value > temp.value:
                    if temp.right == None:
                        temp.right = new_node
                        return True
                    temp = temp.right
                else:
                    print("value already exist")
                    break


    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False    

    def bfs(self):
        queue = []
        res = []
        if self.root == None:
            return []
        queue.append(self.root)
        while len(queue)>0:
            first_node = queue.pop(0)
            res.append(first_node.value)
            left = first_node.left
            right = first_node.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        print(res)
                    

    def print_tree(self):
        # temp = self.root
        pass


tree = BinarySearchTree()
tree.insert(45)
tree.insert(26)
tree.insert(42)
tree.insert(33)
tree.insert(43)
tree.insert(23)

# print(tree.contains(42))
# print(tree.contains(99))

tree.bfs()        
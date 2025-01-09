class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # def insert(self,value):
    #     new_node = Node(value)
    #     if self.root == None:
    #         self.root = new_node 
    #         return
    #     else:      
    #         temp = self.root
    #         while True:
    #                 if temp.left == None:
    #                     temp.left = new_node
    #                     return
    #                 if temp.right == None:
    #                     temp.right = new_node
    #                     return
    #                 left_full = temp.left.left and temp.left.right
    #                 right_full = temp.right.left and temp.right.right

    #                 if not left_full:
    #                     temp = temp.left
    #                 elif not right_full:
    #                     temp = temp.right
    #                 else:
    #                     temp = temp.left

    def insert(self,val):
        queue = []
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return
        queue.append(self.root)
        while len(queue)>0:
            node = queue.pop(0)
            if node.left == None:
                node.left = new_node
                return    
            if node.right == None:
                node.right = new_node
                return
            queue.append(node.left)
            queue.append(node.right)   


 
 #                               43
 #                       56              86
 #                56          96   58         33



tree = BinaryTree()
tree.insert(43)
tree.insert(56)
tree.insert(86)
tree.insert(56)
tree.insert(96)
tree.insert(58)
tree.insert(33)

print(tree.root.right.right.value)




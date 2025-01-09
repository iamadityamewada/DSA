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
    
    

    # def preorder(self):
    #     if self.root == None:
    #         return []
    #     stack =[]
    #     res = []
    #     stack.append(self.root)
    #     while len(stack) > 0:
    #         lastnode = stack.pop()
    #         res.append(lastnode.value)
    #         if lastnode.right:
    #             stack.append(lastnode.right)
    #         if lastnode.left:
    #             stack.append(lastnode.left)
    #     print(res)       

    def preorder(self):
        def traverse(node):
            if node == None:
                return None
            if node:
                print(node.value, end=" ")
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)  
        print("")  

    def postorder(self): 
        def traverse(node):
            if node == None:
                return None
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            if node:
                print(node.value, end=" ")
        traverse(self.root)
        print("")

    def inorder(self):
        result = []
        def traverse(node):
            if node == None:
                return None
            if node.left:
                traverse(node.left)
            if node:
                print(node.value, end=" ")
                result.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root) 
        print("")
        return(result)

    def is_valid_tree(self):
        values = self.inorder()
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                if values[i] > values[j]:
                    return False
        return True 
                                

    def zigzag(self):
        queue = []
        res = []
        if self.root == None:
            return []                
        queue.append(self.root)     
        while len(queue)>0:
            res1 = []
            count = 1
            for i in range(len(queue)):
                f_node = queue.pop(0)
                res1.append(f_node.value)
                left = f_node.left
                right = f_node.right
                if left:
                  queue.append(left) 
                if right:
                  queue.append(right) 
                count +=1               
            # print(res1)            
            if count % 2 == 0:
                res.extend(res1)
            else:
                res1.reverse()
                res.extend(res1) 
            
        print(res)            


tree = BinarySearchTree()
tree.insert(45)
tree.insert(26)
tree.insert(42)
tree.insert(33)
tree.insert(43)
tree.insert(23)
tree.insert(46)
tree.insert(49)
tree.insert(47)
tree.zigzag()

# print(tree.contains(42))
# print(tree.contains(99))

'''
       45  
   26      46  
23    42        49
   33    43  47       


'''

# tree.bfs()  
# tree.preorder()
# tree.postorder()
# tree.inorder()

# print(tree.is_valid_tree())
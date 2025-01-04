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
    
    def getHeight(self):
        if self.root == None:
            return -1
        def height(node):
            if node == None:
                return 0
            if node.left == None and node.right == None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return 1 + max(left_height,right_height)
        return height(self.root)

    def countNode(self):
        if self.root == None:
            return 0
        def count(node):
            if  node == None:
                return 0
            left_count = count(node.left)
            right_count = count(node.right)
            return 1 + left_count + right_count
        return count(self.root)
    

    # def getCount():
    #     c=0               
        
    def get_count_leaf(self):
        if self.root == None:
            
            def count(node):
                if node == None:
                    return 1
                if node.left == None and node.right == None:
                    return 1
                return count(node.left) + count(node.right)
            return count(self.root)            


    def maxMin(self):
        values = self.inorder()
        print("Minimum ", values[0] )
        print("Maximum ", values[len(values)-1])

    def getDepth(self, val):
        if self.root == None:
            return - 1
        temp = self.root
        depth = 0
        while True:
            if temp.value == val:
                break
            elif temp.value > val:
                temp = temp.left
                depth +=1
            elif temp.value < val:
                temp = temp.right
                depth +=1
        return depth 

    def getDiameter(self):
        ls = []
        if self.root == None:
            return -1
        def height(node):
            if node == None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            ls.append(left_height + right_height)
            return 1 + max(left_height,right_height)
        height(self.root)
        return max(ls)   

    def isBalanced(self):
        if self.root == None:
            return True
        self.balanced = True
        def height(node):
            if node == None:
                return True
            if node.left == None and node.right == None:
                return True    
            left_h = height(node.left)
            right_h = height(node.right)
            diff = abs(left_h - right_h)
            if diff > 1:
                self.balanced = False
                return
            return 1 + max(left_h,right_h)        
        height(self.root)
        return self.balanced   

    # def lca(self,p,q):
    #       if self.root == None:
    #         return None
    #       def findlca(node,p,q):
    #         # (p < node.value and q > node.value) or (p > node.value and q < node.value):
    #         temp = node   
    #         if p < temp.value and q < temp.value:
    #             temp = temp.left
    #         elif p > temp.value and q > temp.value:
    #             temp = temp.right
    #         else:
    #             return temp.value
    #         return findlca(temp,p,q)
    #       findlca(self.root,p,q)  
    # 
    
    def lca(self, p , q):
        if self.root == None:
            return None
        temp = self.root
        while True:
            if p < temp.value and  q < temp.value:
                temp = temp.left
            elif p > temp.value and  q > temp.value:
                temp = temp.right
            else:
                return temp.value   

    def sum(self):
        if self.root == None:
            return None
        sum = 0
        def findSum(node):
            nonlocal sum
            if node == None:
                return None
            if node:
                sum += node.value     
            if node.left:
                findSum(node.left)
            if node.right:
                findSum(node.right)
        findSum(self.root)        
        return sum  
    
    def path(self,val):
        if self.root == None:
            return None
        temp = self.root
        path = []
        while True:
            if val < temp.value:
                path.append(temp.value)
                temp = temp.left
            elif val>temp.value:
                path.append(temp.value)
                temp = temp.right
            else:
                break  
        return path      
                


                 


                


tree = BinarySearchTree()
tree.insert(50)
tree.insert(34)
tree.insert(30)
tree.insert(56)
tree.insert(92)
tree.insert(39)
tree.insert(59)

    #          50
    #     34        56   
    # 30     39            92
    #                  59
print(tree.path(39))
# print(tree.sum())          
# print(tree.lca(30,56))
# print(tree.getDepth(59))
# print(tree.getDiameter())
# print(tree.isBalanced())
# print(tree.getHeight())
# print(tree.countNode())
# tree.maxMin()
# print(tree.get_count_leaf())
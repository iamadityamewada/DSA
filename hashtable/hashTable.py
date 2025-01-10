

class HashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = [[] for i in range(size)]
        self.count = 0
        
    def generate_hash_value(self,key):
        hash_value = 0
        prime_number = 31
        key = str(key)
        for i in key:
            hash_value += ord(i)
        return hash_value * prime_number % self.size 

    def insert(self,key,value):
        index = self.generate_hash_value(key)    
        box = self.hash_table[index]
        if len(box) > 0:
            for pair in box:
             if pair[0] == key:
                 pair[1] = value
                 return
        box.append([key,value])

    def print_table(self):
        for ind,box in enumerate(self.hash_table):
           print(f" Index - {ind} {box}")  

    def getValue(self,key):
        index = self.generate_hash_value(key)
        box = self.hash_table[index]
        for pair in box:
            if pair[0]==key:
                return pair[1]
            return "key not found" 

    def getKeys(self):
        keys = []
        for box in self.hash_table:
            for pair in box:
                keys.append(pair[0])
        return keys 

    def delete(self,key):
        index = self.generate_hash_value(key)
        box = self.hash_table[index]
        for pair in box:
            if pair[0]==key:
                box.remove(pair)
        print("Pair deleted")                 
                                        

hashtable = HashTable(10)
hashtable.insert('student','Aditya')
hashtable.insert('student2','Ady')
hashtable.insert('subject','Maths')
hashtable.insert('Roll No',42)
hashtable.insert('tstuden','Adiii')

hashtable.print_table()
# hashtable.getValue("student")
# print(hashtable.getKeys())
hashtable.delete('student2')
hashtable.print_table()







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

hashtable = HashTable(10)
print(hashtable.generate_hash_value("pen"))



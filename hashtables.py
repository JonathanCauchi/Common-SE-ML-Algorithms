class Hashtable:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def print_values(self):
        for i in self.values:
            print(i)
            
    def get(self, key):
        index = self.hashmap(key)
        while(self.keys[index] is not None):
            if(self.keys[index] == key):
                return self.values[index]
        return None #no value in this bucker
    
    def insert(self, key, value): 
        
        index = self.hashmap(key)
        
        while(self.keys[index] is not None): #collision
            if(self.keys[index] == key):
                self.values[index] == value #update
                return
            
            index = (index+1)%self.size
        
        #no collision
        self.keys[index] = key
        self.values[index] = value
        
    def hashmap(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum%self.size

Hash = Hashtable()
Hash.insert("Jon","Gozo Steel")
a = Hash.get("Jon")
print(a)
Hash.print_values()
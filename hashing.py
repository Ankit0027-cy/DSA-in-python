# linear probing
class dicionary:
    def __init__ (self,size):
        self.size=size
        self.slot=[None]*self.size
        self.data=[None]*self.size
        
        
        
    def put(self,key,data):
        hash_value=self.hash_function(key)
        if self.slot[hash_value] == None:
            self.slot[hash_value]=key
            self.data[hash_value]=data
        else:
            if self.slot[hash_value]==key:
                self.data[hash_value]=data
            else:
                new_hash_value=self.rehash(hash_value)
                while self.slot[new_hash_value]!=None and self.slot[new_hash_value]!=key:
                    new_hash_value=self.rehash(new_hash_value)
                if self.slot[new_hash_value]==None:
                    self.slot[new_hash_value]=key
                    self.data[new_hash_value]=data
                else:
                    self.data[new_hash_value]=data
                        
                    
    def __set_item__(self,key,data):
           self.put(key,data)  
    def hash_function(self,key):
        return  abs(hash(key))%self.size
    def rehash(self,old_hash):
        return (old_hash+1)% self.size
    def get(self,key):
        start_position=self.hash_function(key)
        curr_position=start_position
        while self.slot[curr_position]!=None:
            if self.slot[curr_position]==key:
                return self.data[curr_position]
            curr_position=self.rehash[curr_position]
            if curr_position== start_position:
               return "not found"
        return "not found"
    
    def __getitem__(self,key):
        return self.get(key)
    def __str__(self):
        for i in range(len(self.slot)):
            if self.slot[i]!=None:
                print(self.slot[i],' : ', self.data[i], end= "")
d1=dicionary(3)
d1.put("python",4)
d1.put("java",9) 
d1.put("html",6)
d1.put("css",5)
d1.get("java")
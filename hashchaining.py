class Node:
    def __init__(self,value,key):
        self.next=None
        self.value=value
        self.key=key
class linklist:
    def __init__(self):
        self.head=None

        
    def add(self,value,key):
        new_node=Node(value,key)
        if self.head == None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next !=None:
                temp=temp.next
            temp.next=new_node
    def remove(self,key):
        if self.head.key== key:
            self.delele_head()
            return
        if self.head ==None:
            return "empty"
        else:
            temp=self.head
            while temp.next != None:
                if temp.next.key== key:
                    break
                temp=temp.next
            if temp.next == None:
                return "not found"
            else:
                temp.next=temp.next.next
    def delete_head(self):
        if self.head == None:
            return "empty list"
        else:
            self.head=self.head.next 
    def traverse(self):
        temp=self.head
        while temp != None:
            print(temp.key,"--->",temp.value,"--",end="") 
            temp=temp.next  
    def search(self,key):
        temp=self.head
        pos=0
        while temp !=None:
            if temp.key == key:
                return pos
            temp=temp.next
            pos +=1
        return "not found"
    def get_node_at_index(self,index):
        temp=self.head
        counter=0
        while temp != None:
            if counter==index:
                return temp
            temp=temp.next 
            counter +=1
    def size(self):
        temp=self.head
        counter=0
        while temp != None:
            counter +=1
            temp=temp.next
            
        return counter
class dictionary:
    def __init__(self,capcity):
        self.capcity=capcity
        self.size=0
        
         # create array of link list
        self.buckets=self.make_array(self.capcity)    
    def make_array(self,capcity):
        l=[]
        for i in range(capcity):
            l.append(linklist())
        return l
    
    def put(self,key,value):
        bucket_index=self.hash_function(key)
        node_index=self.get_node_index(bucket_index,key)
        if node_index== -1:
            # insert
            self.buckets[bucket_index].add(key,value)
            self.size +=1
            # load_factor=self.size/self.capcity
            # print(load_factor)
            if (self.size/self.capcity>=2):
                self.rehash()
        else:
            # update
            node=self.buckets[bucket_index].get_node_at_index(node_index)
    def rehash(self):
        self.capcity=self.capcity*2
        old_buckets=self.buckets
        self.size
        self.buckets=self.make_array(self.capcity)
        for i in old_buckets:
            for j in range(i.size()):
                node=i.get_node_at_index(j)
                key_item=node.key
                value_item=node.value 
                self.put(key_item,value_item)                   
            
    def hash_function(self,key):
        return abs(hash(key)) % self.capcity
    def get_node_index(self,bucket_index,key):
        node_index= self.buckets[bucket_index].search(key)
        return node_index 
    def __setitem__(self,key,value):
        self.put(key,value)
    def get(self,key):
        bucket_index=self.hash_function(key)
        res=self.buckets[bucket_index].search(key)
        if res== None:
            return "not found"
        else:
            node=self.buckets[bucket_index].get_node_at_index(res)
            return Node.value
    def get_item(self,key):
        return self.get(key) 
    def delete_item(self,key):
        bucket_index=self.hash_function(key)
        self.buckets[bucket_index].remove(key)
    def __str__(self):
        for i in self.buckets:
            i.traverse()
            return "data"
    
        
ll=linklist()
# ll.add("p",1)
# ll.add("r",5)
# # ll.remove()
# ll.traverse()
# ll.search(5)              
d1=dictionary(4)
d1.put("r",5)
d1.put("p",8)
d1.put("q",7)
d1.put("a",11)
d1.delete_item("r")


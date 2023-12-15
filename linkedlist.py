# linked list singly
class Linkedlist:
    class Node: 
       def __init__(self,value):
           self.value=None
           self.next=None
    #constructer of linked list 
       def __init__(self):
           self.head= None
           self.size=0
       def length(self):
           return self.size
       def is_empty(self):
           return self.size == 0
       def print_ll(self):
           temp=self.head
           while temp != None:
               print(temp.value, end=" ")
               temp=temp.next 
        
       def add_head(self,data):
    
           new_node=self.Node(data,self.head)
           new_node.next=self.head
           self.head=new_node
        #    self.head=self.Node(value,self.head)
        #    self.size += 1
       def sorted(self, value):
           new_node=self.Node
ll =Linkedlist()           
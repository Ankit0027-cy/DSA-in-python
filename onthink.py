# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class linklist:
#     def __init__(self) -> None:
#         self.head=None
#         self.size=0
#     def length(self):
#         return self.size
#     def is_empty(self):
#         return self.size == 0
#     def printll(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data, end="")
#             temp=temp.next
#         print()
    
#     def insert(self,data):
#         new_node=node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def append(self, data):
#         new_node=node(data)
#         temp=self.head
#         if self.head == node:
#             self.head=new_node
#             return
#         while temp.next is not None:
#             temp=temp.next
#         temp.next=new_node
#         self.size +=1
    
#     # def sort_insert(self, value):
#     #     new_node=node(value)
#     #     temp=self.head
#     #     if temp == None or temp.value > value:
#     #         new_node=self.head
#     #         self.head=new_node
#     #         return
#     #     while temp.next is not None and temp.next.value<value:
#     #         temp=temp.next
#     #         new_node.next=temp.next 
#     #         temp.next=new_node
#     def find(self,data):
#         temp=self.head
#         while temp is not None:
#             if temp.data == data:
#                 return True
#             else:
#                 return False
#             temp=temp.next
            
#         return False
#     def removestart(self):
#         if self.is_empty():
#             raise RuntimeError("empty list")
#         value=self.head.data
#         self.head=self.head.next
#         self.size -=1
#         return value
    
#     def remove(self,value):
#         temp=self.head
#         if self.is_empty():
#             return False
#         if value == self.head.data:
#            self.head= self.head.next
#            return True
#         while temp.next is not None:
#             if temp.next.data == value:
#                temp =temp.next.next 
#                self.size -=1
#                return True
#             temp = temp.next
#     def free(self):
#         self.head=None
#         self.size=0
#     def reverse(self):
#         temp= self.head
#         prev=None
#         while temp is not None:
#             nextval=temp.next
#             temp.next=prev
#             prev=temp
#             temp=nextval
#             self.head=prev
#     def removeduplicate(self):
#         temp=self.head
#         while temp is not None:
#             if temp.next is not None and temp.data == temp.next.data:
#                  temp.next=temp.next.next 
#             else:
#                    temp=temp.next
#     #copy list reversed
#     def copy_listreversed(self):
#         temp_node=None
#         temp=self.head
        
#         while temp is not None:
#             temp_new_node=node(temp.data,temp_node)
#             temp=temp.next
#             temp_node=temp_new_node
#     def length(self):
#         temp= self.head
#         count=0
#         while temp is not None:
#             count +=1
#             temp=temp.next
#         return count
            
        
# ll=linklist()
# ll.insert(1)
# ll.insert(2)
# ll.insert(3)
# ll.append(4)
# ll.append(5)
# ll.insert(1)
# # ll.find(9)
# # ll.removestart()
# # ll.remove(2)
# # ll.free()
# # ll.reverse()
# # ll.removeduplicate()
# # ll.copy_listreversed()
# ll.length()

# ll.printll()
# class Node:
#     def __init__(self,data,next,prev):
#         self.data=data
#         self.next=None
#         self.prev=None
# class Dublyll:
#     def __init__(self):
#         self.head=None
#         self.tial=None
#         self.count=0
        
#     def size(self):
#         return self.count 
#     def is_empty(self):
#         return self.size() ==0
#     def printdll(self):
#         temp=self.head
#         while temp is not None:
#             print(temp.data, end="")
#             temp=temp.next
#         print()
#     def inserthead(self,data):
#         self.count +=1
#         if self.head is None:
#             self.tial=self.head
#             self.head=Node(data,None,None)
            
#         else:
#             new_node=Node(data,self.head,None)
#             self.head.prev=new_node
#             self.head=new_node
            
            
#     def sorted_insert(self,data,value):
#         temp=Node(data,self.head,None)
#         curr=self.head
#         self.count += 1
        
#         if curr == Node:
#             # first elment
#             self.head=temp
#             self.tial=temp
#             return
#         if curr.value >= data:
#             temp.next=self.head
#             self.head.prev=temp
#             self.head=temp
#             return
#         while curr is not None & curr.next.data < value:
#             curr=curr.next
#         if  curr.next == None:
#             self.tail=temp
#             self.prev=curr
#             curr.next=temp
#         else:
#             temp.next=curr.next
#             temp.prev= curr
#             curr.next=temp
#             temp.next.prev=temp
    
#     def remove_head(self):
#         if self.is_empty():
#             raise RuntimeError("dll is empty")
#         self.count -=1
#         value = self.head.data
#         self.head=self.head.next
#         if self.head == None:
#             self.tail=None
#         else:
#             self.head.prev=None
            
#         return value
#     def remove_node(self,key):
#         temp=self.head
#         if temp == None:
#             return 'empty list'
#         if temp.data==key:
#             self.head= self.head.next
#             if self.head is not None:
#                self.head.prev=None
#             else:
#                 self.tail=None
#         while temp.next is not None:
#             if temp.next.data == key:
#                 temp.next=temp.next.next 
#                 if temp.next is None:
#                     self.tail=temp
#                 else:
#                     temp.next.prev=temp
#                     self.count -=1
#                     return True
#                 temp=temp.next
#         return False
    
#     def remove_duplicate(self):
#         temp=self.head
#         while temp is not None:
#             if (temp.next is not None)and temp.data ==temp.next.data:
#                 temp.next=temp.next.next 
#                 if temp.next is not None:
#                     temp.next.prev=temp
#                 else:
#                     self.tail=temp
                    
#             else:
#                 temp=temp.next
                
#     def reverselilst(self):
#         temp=self.head
#         while temp is not None:
#             new_node=temp.next
#             temp.next=temp.prev
#             temp.prev=new_node
#             if temp.prev is None:
#                 self.tail=self.head
#                 self.head=temp
#                 return
#             temp=temp.prev
#         return
                    
# dll=Dublyll()
# dll.inserthead(1)
# dll.inserthead(2)
# dll.inserthead(5)
# dll.inserthead(8)
# dll.inserthead(7)
# dll.inserthead(4)
# dll.inserthead(0)
# dll.remove_head()
# dll.remove_node(5)
# for i in range(3):
#     dll.inserthead(i)
#     dll.inserthead(i)
    
# print()
# dll.printdll()
# dll.remove_duplicate()
# dll.printdll()
# dll.reverselilst()
# dll.printdll()
class circulerlist:
 class Node:
    def __init__(self,data):
        self.data=data
    def __ini__(self):
        self.tail=None
                




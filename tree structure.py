class Tree:
        def __init__(self, data):
            self.data=data
            self.left=None
            self.right=None
            self.size=0
        # def show(self):
        #     if self.left:
        #         self.left.show()
        #     print(self.data) 
        #     if self.right:
        #         self.right.show()   
        def insert(self,data):
            if self.data is None:
                self.data=data
                return
            if self.data == data:
                return "data already exist"
            if self.data> data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left=Tree(data)
                    
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right=Tree(data)
        def search(self,data):
            if self.data == data:
                print("node is found!")
                return
            if data<self.data:
                if self.left:
                    self.left.search(data)
                else:
                    print("node is not present")
            else:
                if self.right:
                    self.right.search(data)
                else:
                    print("node is not present")
        def pre_order(self):
            print(self.data)
            if self.left:
                self.left.pre_order()
            if self.right:
                self.right.pre_order() 
        def inorder(self):
            if self.left:
                self.left.inorder()
            print(self.data)
            if self.right:
                self.right.inorder() 
        def post_order(self):
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
            print(self.data)  
            
        def delete(self,data):
            if self.data is None:
               print('tree is empty')
               return
            if data< self.data:
                if self.left:
                  self.left=self.left.delete(data)
                else:
                    print("given node is not present")  
            elif data>self.data:
                if self.right:
                    self.right=self.right.delete(data)
                else:
                    print("given node is not present") 
            else:
                if self.left is None:
                    temp=self.right
                    self=None
                    return temp
                if self.right is None:
                    temp=self.left
                    self=None
                    return temp
                node=self.right
                while node.left:
                    node=node.left
                self.data=node.data
                self.right=self.right.delete(node.data) 
        def min_node(self):
            curr=self
            while curr.left is not None:
                curr=curr.left
            print("node with smallest key is : ", curr.data)
        def max_node(self):
            curr=self
            while curr.right:
                curr=curr.right
            print("node with the maximam data is :", curr.data)
                
        
root=Tree(10)
root.insert(7)
root.insert(8)
root.insert(12)
root.insert(9)
root.insert(14) 
root.insert(18)
# root.search(7)
# root.pre_order()
# root.inorder()
# root.delete(10)
# root.pre_order()
root.min_node()
root.max_node()
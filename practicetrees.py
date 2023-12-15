# from queue import Queue
# q=Queue

class Tree:
    def __init__(self,data) -> None:
        self.left=None
        self.right=None
        self.data=data
        self.level=None
       
    def Node(self,data):
        if self.data:
            if self.data>data:
                if self.left is None:
                    self.left=Tree(data)
                else:
                    self.left.Node(data)
            elif self.data<data:
                if self.right is None:
                    self.right=Tree(data)
                else:
                    self.right.Node(data)
            else:
                self.data=data
    def preorder(self):
        if self.data:
            print(self.data)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right. preorder()
        else:
            return -1
    
    def postorder(self):
        if self.data:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data)
        else:
            return -1
    def inorder(self):
        if self.data:
            if self.left:
                self.left.inorder()
            print(self.data)
            if self.right:
                self.right.inorder()
        else:
            return -1        


    def hieght(self):
        if root is None:
            return -1
        return max(self.hieght(root.left),self.hieght(root.right))+1
    from queue import Queue    
    def levelorder(self):
       if self.data is None:
           
        que=[root]
        while len(que)>0:
            node=que.pop(0)
            node.visit()
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
       
    def search(self,data):
        if self or self.data== data: 
            return
        if data<self.data:
            return self.search(self.left, data)
        return self.search(self.right,data)
    def delete(self,data):                                                                                                                                                
        self.root=self.node._delete(self.root,data)
        
    def _delete(self,data ,node):
        if node ==None:
            return self.Node
        if data<self.node:            self.left=node.delete(self.left,data)
        elif data>self.data:
            self.right=node.delete(self.right,node)
            
        
    def min_value(self):
        while self.left is not None:
            node=self.left
            return node.data
    def max_value(self):
            while self.right is not None:
                node=self.right
                return node.data
    def bst(root,minvlaue,maxvalue):
        if root is None:
            return True
        
            
root=Tree(10)
root.Node(50)
root.Node(30)
root.Node(80)
root.Node(70)
root.Node(60)
root.Node(5)
root.Node(7)
root.Node(9)
# root.Node(8)
# root.levelorder()
root.delete(7)
# print(" preorder")
# root. preorder()
# print("postorder")
# root.postorder()
# print("inorder")
# root.inorder()
# print(root.hieght(root))
# root.level_order()
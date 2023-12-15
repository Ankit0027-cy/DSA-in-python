# class Node:
#     def __init__(self,data) -> None:
#         self.left=None
#         self.right=None
#         self.data=data
        
        
#     def show(self):
#         if self.left:
#             self.left.show()
#         print(self.data)
#         if self.right:
#             self.right.show()
            
            
# root=Node(100)
# r_left=Node(99)
# r_right=Node(101)
# root.left=r_left
# root.right=r_right
# root.show()
class Node:
    def __init__(self,value) -> None:
        self.left=None
        self.right=None
        self.data=value
class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
            temp=self.root
            parent=temp
        if data< node.data:
            node.left=self.insert(node.left,data)
        else:
            self.right=self.insert(node.right,data)
        return node
        if node.value< parent.value:
                    parent.left=node
        else:
          
                    parent.right=node
    
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
#driver code
tt = Tree()
root=tt.createNode(5)
tt.insert(root,2)
tt.insert(root,3)
tt.insert(root,6)
tt.insert(root,4)
tt.insert(root,8)
tt.insert(root,7)
tt.insert(root,9)
tt.insert(root,11)
tt.inorder(root)
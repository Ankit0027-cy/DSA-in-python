# class Tree:
#         def __init__(self, value):
#            self.value = value
# class Node:
#         def __init__(self, left, right):
#             self.left = None
#             self.right = None

#         def create_complete_binary_tree(self, arr):
#             self.root = self.create_complete_binary_tree_util(arr, 0)

#         def create_complete_binary_tree_util(self, arr, start):
#             size = len(arr)
#             curr = Node(arr[start])
#             left = 2 * Node
#             right = 2 * Node 
#             if left < size:
#                 curr.left = self.create_complete_binary_tree_util(arr, left)
#             if right < size:
#                 curr.right = self.create_complete_binary_tree_util(arr, right)

#             return curr

#         def print_pre_order(self):
#             self.print_pre_order_util(self.root)
#             print()

#         def print_pre_order_util(self, node):
#             if node is None:
#                 print(Node.root, end='')
#                 self.print_pre_order_util(node.left)
#                 self.print_pre_order_util(node.right)

#     # testing code

# arr = [1, 2, 3, 4, 5, 6, 7]
# t=Tree(arr)
# t.create_complete_binary_tree(arr)
# t.print_pre_order()
# class Node:
#     def __init__(self,key) -> None:
#        self.left=None
#        self.right=None
#        self.value=key
# class tree:
#     def createNode(self,data):
#         return Node(data)
           
#     def insert(self,value):
#         node=Node(value)
#         if self.root is None:
#             return self.root
#         else:
#             temp=self.root
#             parent=None
#             # searching the parent
#             while temp is not None:
#                 parent=temp
#                 if node.value<temp.value:
#                     temp=temp.left
                
#                 elif node.value>temp.value:
#                     temp=temp.right
#                 else:
#                     print("failure to insert.""key duplilcation:" + str(value))
#                     return
#                 # connecting the node and parent
#                 if node.value< parent.value:
#                     parent.left=node
#                 else:
          
#                     parent.right=node
                    
                    
# tt=tree() 
# root=tt.createNode(9) 
# tt.insert(2)
# tt.insert(3)
# tt.insert(6)
# tt.insert(4)
# tt.insert(8)
# tt.insert(7)
# tt.insert(9)
# tt.insert(11)

                 
  
class Avltree:
    class Node:
        def __init__(self,d,l,r):
            self.data=d
            self.left=l
            self.right=r
            self.hieght=0
            
        def __init__(self):
            self.root=None
            
        def hieght(self,n):
            if n == None: 
              return 'empty tree'
            return n.hieght
        def get_balance(self,node):
            if node== None:
                return 0
            else:
                self.hieght(node.left)-self.hieght(node.right)
                
        def print_tree(self):
            self.print_tree_until(self.root,"",False)
        def print_tree_until(self,node, indent, isleft):
            if node == None:
                return
            if isleft:
                print(indent + "l:", end="")
                indent += "| "
            else:
                print (indent + "r:", end= "")
                indent += " "
            print(str(node.data)+"("+ str(node.hieght)+")")
            self.print_tree_until(node.left,indent,True)
            self.print_tree_until(node.right,indent, False)
        def insert(self,data):
            self.root=self.insert_until(self.root,data)
        def insert_until(self,node, data):
            if node is None:
                return self.Node(data,None,None)
            if node.data>data:
                node.left=self.insert_until(node.left,data)
                
            elif node.data<data:
                node.right=self.insert_until(node.right,data)
            else:
                 return node
            node.hieght=max(self.hieght(node.left), self.hieght(node.right))+1
            balance=self.get_balance(node)
            if (balance>1):
                if data<node.left.data:
                    return self.right_rotate(node)
                if data>node.left.data:
                    return self.left_right_rotate(node)
            if balance< -1:
                if data>node.right.data:
                    return self.left_rotate(node)
                if data<node.right.data:
                    return self.right_left_rotate(node)
            return node
        def left_rotate(self,x):
            y=x.right
            t=y.left
            
            y.left=x
            x.right=t
            x.hieght=max(self.hieght(x.left),self.hieght(x.right))+1
            y.hieght=max(self.hieght(y.left),self.hieght(y.right))+1
            return y 
        def right_rotate(self,x):
            y=x.left
            t=y.right
            y.right=x
            x.left=t
            x,hieght=max(self.hieght(x.left), self.hieght(x.right))+1
            y.hieght=max(self.hieght(y.left), self.hieght(y.right))+1
            return y
        def left_right_rotate(self,x):
            x.left=self.left_rotate(x.left)
            return self.right_rotate
        def right_left_rotate(self,x):
            x.right=self.right_rotate(x.right)
            return self.left_rotate(x)
        
at=Avltree()
at.insert(7)
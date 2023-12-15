class Node:
    def __init__ (self,data,parent=None):
        self.data=data
        self.parent=parent
        self.height=0
        self.left=None
        self.right=None
class Avltree:
    def __init__(self):
        self.__root=None
    def insert(self,data):
        # if there is no "root node"
        if self.__root ==None:
            self.__root=Node(data)
        else:
            self.__insert_data(data,self.__root)
            
    def __insert_data(self,data,node):
        if data<node.data:
            if node.left:
                self.__insert_data(data,node.left)
            else:
                node.left=Node(data,node)
                self.__violation_handler(node.left)
        if data>node.data:
            if node.right:
                self.__insert_data(data,node.right)
            else:
                node.right=Node(data,node)
                self.__violation_handler(node.right)
    def remove(self,data):
        if not self.__root:
            print("No data")
        else:
            self.remove_data(data,self.__root)
    def remove_data(self,data,node):
        #  first i would find the data
        if data<node.data:
            if node.left:
                self.remove_data(data,node.data)
        elif data>node.data:
            if node.right:
                self.remove_data(data,node.data)
        elif data==node.data:
            # when the node to the removed for no child; leaf node
            if not node.left and not node.right:
                parent_node=node.parent
                if parent_node:
                    if parent_node.left== node:
                        parent_node.left=None
                    elif parent_node.right==node:
                        parent_node.right=None
                # if the node is root node
                else:
                    self.__root=None
                    del node
                    self.__violation_handler(parent_node)
            #when the left node is  exists
            elif node.left and not node.right:
                parent_node=node.parent
                # parent to child relationship
                if parent_node:
                    if parent_node.left==node:
                        parent_node.left=node.left
                    elif parent_node.right== node:
                        parent_node.right=node.left
                else:
                    self.__root=node.left
                    # child to parent relationship
                    node.left.parent=parent_node
                    del node
                    self.__violation_handler(parent_node)
            #  when right child exists
            elif node.right and not node.left:
                parent_node=node.parent
                # parent to child relationship
                if parent_node:
                    if parent_node.left==node:
                        parent_node.left=node.right
                    elif parent_node.right== node:
                        parent_node.right=node.right
                else:
                    self.__root=node.right
                    # child to parent relationship
                    node.right.parent=parent_node
                    del node
                    self.__violation_handler(parent_node)
            #  when the node has two children 
            #  we have the find the either the predecessor and successer node 
            # swap the values of the node and either of the above mentioned nodes
            #  delete the predicssesser and succsesser
            elif node.left and node.right:
                #  succusser node is a smallest node in a right subtree of the node
                succusser_node=self.find_succusser(node.right)
                [succusser_node.data],[node.data]=[node.data],[succusser_node.data] 
                self.remove_data(succusser_node.data, node.right)
                
    def succusser(self,node):
                if node.left:
                    return self.succusser(node.left)
                return node
           
    def __violation_handler(self,node):
        while node:
            node.height=max(self.calculate_height(node.left), self.calculate_height(node.right))+1
            self.violation_fix(node)
            node=node.parent
    def calculate_height(self,node):
        if not node:
            return -1
        return node.height
    def violation_fix(self,node):
        # left left case:
        if self.balance_factor(node)>1:
            # left right 
            if self.balance_factor(node.left)< 0:  #1 give me as infinteloop
                self.rotate_left(node.left)
            self.rotate_right(node)
            # right right case
        if self.balance_factor(node)<-1: 
            # right left case
            if self.balance_factor(node.right)>0: #avoid the infinte loop
               self.rotate_right(node.right)
            self.rotate_left(node)
               
            
            
    def balance_factor(self,node):
        if not node:
            return 0
        return self.calculate_height(node.left)-self.calculate_height(node.right)
    def rotate_left(self,node):
        temp_right_node=node.right
        t=node.right.left
        # updating the references
        temp_right_node.left=node
        node.right=t
        # update child to parent relationship
        temp_parent=node.parent
        temp_right_node.parent=temp_parent
        node.parent=temp_right_node
        if t:
            t.parent=node
            
        # update parent to child relationship
        if temp_right_node.parent:
           if temp_right_node.parent.left== None:
              temp_right_node.parent.left=temp_right_node
           elif temp_right_node.parent.right== None:
               temp_right_node.parent.right=temp_right_node
        # if it is a root node
        else:
            self.__root=temp_right_node
        #  update the hieght of the nodes
        node.height=max(self.calculate_height(node.left),self.calculate_height(node.right))+1
        temp_right_node.height=max(self.calculate_height(temp_right_node.left),self.calculate_height(temp_right_node.right))+1
        
        # print("left rotation data",(node.data),"...")
        return node.data
    def rotate_right(self,node):
        temp_left_node=node.left
        t=node.left.right
        # update the references
        temp_left_node.right=node
        node.left=t
        # child to parent
        temp_parent=node.parent
        temp_left_node.parent=temp_parent
        node.parent=temp_left_node
        if t:
            t.parent=node
        # parent to child
        if temp_left_node.parent:
            if temp_left_node.parent.left==node:
                temp_left_node.parent.left=temp_left_node
            elif temp_left_node.parent.right==node:
                temp_left_node.parent.right=temp_left_node
                
        else:
            self.__root=temp_left_node
            # update the height of the nodes
            node.height=max(self.calculate_height(node.left),self.calculate_height(node.right))+1
            temp_left_node.height=max(self.calculate_height(temp_left_node.left),self.calculate_height(temp_left_node.right))+1
            # print("left rotation on"(node.data),"...")
            return node.data
                
    def traverse(self):
        if self.__root:
            self.inorder(self.__root)
    def inorder(self,node):
        if node.left:
            self.inorder(node.left)
        print(node.data)
        if node.right:
            self.inorder(node.right)
    def find(self,data):
        # find the data 
        if self.__root:
            return self.find_data(data,self.root)
    def find_data(self):
        
if   __name__ == " __main__ ":
    tree=Avltree()
    tree.insert(12)
    tree.insert(15)
    tree.insert(74)
    tree.insert(7)
    tree.insert(9)
    tree.insert(14)
    tree.insert(16)
    tree.traverse()
    tree.remove(7)
    
                    
class node :
    def __init__(self,data,next):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top= None
        self.bottom =None
        self.size=0
        
        
    def size(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def peek(self):
        # if self.is_empty():
        #     raise RuntimeError('empty list')
        return self.top.data
    def push(self,data):
        new_node=node(data,next=None)
        if self.bottom == None:
            self.bottom=new_node
            self.top=self.bottom
        else:
            self.top.next=new_node
            self.top=new_node
            self.size +=1
    def pop(self):
        temp=self.bottom
        temp=temp.next
        self.size -=1
        temp=temp.next
    def print(self):
        temp=self.bottom
        box=[]
        while temp is not None:
            box.append(temp.data)
            temp=temp.next
        return box       
st=stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.pop()
st.print()
st.peek()
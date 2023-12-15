class stack:
    def __init__(self):
        self.stack=list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self) -> str:
        return str(self.stack)
st=stack()
st.push(1)
st.push(4)
st.push(3)
st.push(2)
st.peek()
st.pop()
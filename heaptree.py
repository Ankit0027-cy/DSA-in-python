class Heap:
    def __init__(self,capacity):
        self.storage=[0]*capacity
        self.capacity=capacity
        self.size=0
         
    def  getparentindex(self,index):
        return (index-1)//2
    def getleftindex(self,index):
        return 2*index+1
    def getrightindex(self,index):
        return 2*index+2
    def hasparent(self,index):
        return self.getparentindex(index)>=0
    def hasleftchild(self,index):
        return self.getleftindex(index)>=self.size
    def hasrightchild(self,index):
        return self.getrightindex(index)>self.size
    def isfull(self):
        return self.size== self.capacity
    def swap(self,index1,index2):
        temp=self.storage[index1]
        self.storage[index1]=self.storage[index2]
        self.storage[index2]=temp
    def insert(self,data):
        if self.isfull():
            raise("heap is full")
        return
        self.storage[self.size]=(data)
        self.size +=1
        self.heapfiyup()
    def heapfiyup(self):
       index=self.size -1
       while (self.hasparent(index)and self.hasparent(index)> self.storage[index]):
           self.swap(self.getparentindex(index),index)
           index=self.getparentindex(index)
    def removemin(self):
        index=0
        while self.hasleftchild(index):
            smallerchild=self.getleftindex(index)
            if self.hasrightchild(index)and self.getrightindex(index)< self.getleftindex(index):
                smallerchild=self.getrightindex(index)
                if self.storage(index)<self.storage[smallerchild]:
                    break
                else:
                    self.swap(index,smallerchild)
                    index=smallerchild
    def print(self):
        temp=self.storage
        while temp is not None:
            print(self.storage)
                
hp=Heap(7)
hp.insert(5)
hp.insert(25)
hp.insert(4)
hp.insert(45)
hp.insert(65)
hp.insert(8)
hp.insert(12)
hp.insert(15)
hp.insert(35)
hp.print()
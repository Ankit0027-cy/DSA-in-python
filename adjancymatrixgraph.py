# adjency matrix graph
class Graph:
    def __init__(self,size):
        self.size=size #vertices_no
        self.graph=[]
        self.vertex=[]
    def add_vertex(self,v):
        if v in self.vertex:
           pass
        else:
            self.vertex.append(v)
            temp=[]
            for i in range(self.size):
                temp.append(0)
            self.graph.append(temp)
    def add_edges(self,v1 ,v2 ,e):
        i1=self.vertex.index(v1)
        i2=self.vertex.index(v2)
        self.graph[i1][i2]=e
    def rem_edge(self,v1,v2):
        i1=self.vertex.index(v1)
        i2=self.vertex.index(v2)
        self.graph[i1][i2]=0
        
    def printgrap(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.vertex[i],"-->",self.vertex[j], "edge weight",self.graph[i][j])
gr=Graph(4)
# add vertex
gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)
gr.add_vertex(4) 
# add edges
gr.add_edges(1,2,1)
gr.add_edges(1,3,1)
gr.add_edges(2,3,3)
gr.add_edges(3,4,4)
gr.add_edges(4,1,5)
gr.printgrap()
print(gr.graph)
   
# graph implementation using adjancency list
class Graph:
    def __init__(self,size):
        self.size=size #vertex_no
        self.graph={}
        
    def add_vertex(self,v):
        self.graph[v]=[]
    def add_edge(self,v1,v2,e):
        temp=[v2,e]
        self.graph[v1].append(temp)
    def del_edge(self,v1,v2):
        self.graph[v1].pop(0)
    def printgraph(self):
        self.graph
        for i in self.graph:
            for j in self.graph[i]:
                print(i ,"-->",j[0],"edge weight",j[1])
gr=Graph(4)
gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)
gr.add_vertex(4)
print(gr.graph)
gr.add_edge(1,2,1)
gr.add_edge(1,3,1)
gr.add_edge(2,3,3)
gr.add_edge(3,4,4)
gr.add_edge(4,1,5)
gr.printgraph()

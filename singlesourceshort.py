def ssspath(graph,node,d,dist,par):
    dist[node]=d
    for child in graph[node]:
        if child != par:
            ssspath(graph,child,dist[node]+1,dist,node)
        
edges=[['A','B'],['A','C'],['C','E'],['C','F']]
nodes=['A','B','C','D','E','F','G','H','I']


graph={}
dist={}
for key in nodes:
    graph[key]=[]
    dist[key]=None
for (u,v)in edges:
    graph[u].append(v)
    graph[v].append(u)
start='A'
dist[start]=0
ssspath(graph,start,0,dist,-1)
for key,vlaue in dist.items():
    print(key,vlaue)


 
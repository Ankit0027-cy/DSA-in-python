def dfs(graph,visited,node):
    visited[node]=True
    sm=0
    for child in graph[node]:
        if not visited[child]:
            sm=max(sm,dfs(graph,visited,child))
    return sm+1
def dfs1(graph,visited,node):
    visited[node]=True
    sm=0
    temp=node
    for child in graph[node]:
        if not visited[child]:
            (tvalue,tnode)=dfs1(graph,visited,child)
            if tvalue>sm:
                temp=tnode
                sm=tvalue
    return sm+1,temp


ipt=[[1,2],[2,4],[2,5],[2,6],[1,3],[3,7],[1,8],[6,10],[1,9]]
n=10




graph={}
visited={}

for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    
for (u,v)in ipt:
    graph[u].append(v)
    graph[v].append(u)

# temp=dfs(graph,visited,1)
# print(temp)
temp=dfs1(graph,visited,1)
v={}
for i in range(1,n+1):
    v[i]=False
print(dfs(graph,v,temp[1]))
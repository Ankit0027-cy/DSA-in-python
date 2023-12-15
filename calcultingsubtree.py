def dfs(graph,visited,node,distance):
    visited[node]=True
    sm=0
    for child in graph[node]:
        if not visited[child]:
            sm=(sm+dfs(graph,visited,child,distance))
    distance[node]=sm+1
    return distance[node]

ipt=[[1,2],[2,4],[2,5],[2,6],[1,3],[3,7],[1,8],[6,10],[1,9]]
n=10




graph={}
visited={}
distance={}

for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    
for (u,v)in ipt:
    graph[u].append(v)
    graph[v].append(u)

temp=dfs(graph,visited,1,distance)
print(distance)
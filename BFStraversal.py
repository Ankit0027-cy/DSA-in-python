def bfs(graph,visited):
    queue=[]
    queue.append(1)
    visited[1]=True
    while queue:
        temp=queue.pop(0)
        print(temp)
        for child in graph[temp]:
            if not visited[child]:
                queue.append(child)
                visited[child]=True
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
temp=bfs(graph,visited)
print(temp)
#  topological search using khan'a algoritham
def kahn(graph,visited,indegree):
    queue=[]
    for key in visited:
        if indegree[key] ==0:
            queue.append(key)
            visited[key]=True
        # print(indegree)
            
    while queue:
        temp=queue.pop(0)
        # print(temp)
        for child in graph[temp]:
            if not visited[child]:
                indegree[child]-=1
                if indegree[child]==0:
                    queue.append(child)
                    visited=True
        
    
ipt=[[1,2],[2,3],[1,3],[4,1],[6,1],[4,3],[5,3],[8,1],[1,7],[9,8],[9,7]]
n=9




graph={}
visited={}
indegree={}

for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    indegree[i]=0
    
for (u,v)in ipt:
    graph[u].append(v)
    indegree [v]+=1
# print(indegree)
# # temp=dfs(graph,visited,1)
# print(temp)
# temp=bfs(graph,visited)
# print(temp)
temp=kahn(graph,visited,indegree)
print(temp)
def dfs(graph,node,visited,intime,outtime):
    global timer
    intime[node]=timer
    timer +=1
    visited[node]=True
    for child in graph[node]:
        if not visited[child]:
            dfs(graph,child,visited,intime,outtime)
    outtime[node]=timer
    timer +=1
            
ipt=[[1,2],[2,4],[2,5],[2,6],[1,3],[3,7],[3,8]]
n=8
graph={}
visited={}
intime={}
outtime={}
timer=1

for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    
for (u,v)in ipt:
    graph[u].append(v)
    graph[v].append(u)
dfs(graph,1,visited,intime,outtime)
print(intime)
print(outtime)
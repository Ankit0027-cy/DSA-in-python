def dfs(graph,visited,node,intime,lowtime,parent):
    global timer
    global root
    visited[node] =True
    intime[node]=timer
    lowtime[node]=timer
    timer +=1
    c=0
    
    for child in graph[node]:
        if not visited[child]:
            if node== root:
                c+=1
            dfs(graph,visited,child,intime,lowtime,node)
            if intime[node]<lowtime[child] and node!=root:
                print ('articulatio point--{}'.format(node))
            lowtime[node]=min(lowtime[node],lowtime[child])
        else:
            if child != parent:
                lowtime[node]=min(lowtime[node],intime[child])
        if c>1:
            print('articulation point ->',node)
                   
ipt=[[1,2],[2,3]]
n=3
graph={}
visited={}
# distance={}
intime={}
lowtime={}


for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    intime[i]=None
    lowtime[i]=None
for (u,v)in ipt:
    graph[u].append(v)
    graph[v].append(u)
timer=1
root=1
dfs(graph,i,visited,-1,intime,lowtime )
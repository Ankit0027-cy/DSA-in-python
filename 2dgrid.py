grid=[[3,1,5],[7,8,2],[14,11,9]]
row=len(grid)
col=len(grid[0])
visited=[]
for _ in range(row):
    temp=[]
    for _ in range(col):
        temp.append(0)
    visited.append(temp)
for item in visited:
    print(item)

def dfs(grid,visited,start):
    x,y=start[0],start[1]
    print(grid[x][y])
    visited[x][y]=1
    if isvalid(grid,visited,x,y+1):
        dfs(grid,visited,(x,y+1))
        visited[x][y+1]=1
    if isvalid(grid,visited,x,y-1):
        dfs(grid,visited,(x,y-1))
        visited[x][y-1]=1
    if isvalid(grid,visited,x+1,y):
         dfs(grid,visited,(x+1,y))
         visited[x+1][y]=1
    if isvalid(grid,visited,x-1,y):
         dfs(grid,visited,(x-1,y))
         visited[x-1][y]=1
def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited [x][y]==1:
        return False
    return True
dfs(grid,visited,(0,0))
    
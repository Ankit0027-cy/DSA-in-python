def dfs(grid,visited,start):
    i,j=start[0],start[1]
    visited[i][j]=1
    sm=0
    for a,b in [[1,0],[0,1],[-1,0],[0,-1]]:
        if isvalid(grid,visited,i+a,j+b):
            sm+=dfs(grid,visited,(i+a,j+b))
    return sm+1
def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1 or grid[x][y]==1:
        return False
    return True

grid=[[0,1,0,0,0][0,0,1,1,0,0],
      [1,0,0,1,0,0],
      [1,1,0,1,0,0]]
visited=[]
row=len(grid)
col=len(grid[0])
for _ in range(row):
    temp=[]
    for _ in range(col):
        temp.append(0)
    visited.append(temp)
# for item in visited:
#     print(item)
answer=[]
for i in range(row):
    for j in range(col):
        if visited[i][j]==0 and grid[i][j]==0: 
            temp=dfs(grid,visited,(i,j))
            answer.append(temp)

print(answer)
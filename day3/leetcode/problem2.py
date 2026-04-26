# 1559. Detect Cycles in 2D Grid


grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
row=len(grid)
col=len(grid[0])
visited=[]

for i in range(row):
    visited.append([False]*col)
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(i,j,grid,visited,pi,pj):
    visited[i][j]=True

    for di,dj in directions:
        ni=i+di
        nj=j+dj

        if 0<=ni<row and 0<=nj<col and grid[i][j]==grid[ni][nj] :
            if (ni,nj)==(pi,pj):
                continue
            if visited[ni][nj]:
                return True
            if dfs(ni,nj,grid,visited,i,j):
                return True
    return False


for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            if dfs(i,j,grid,visited,-1,-1):
                print(True)

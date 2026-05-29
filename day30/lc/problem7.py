# 695. Max Area of Island


def maxAreaOfIsland(grid):
    rows=len(grid)
    col=len(grid[0])
    mxarea=0
    visited=set()
    def dfs(r,c):
        if r<0 or c<0 or r>=rows or c>=col:
            return 0
        if grid[r][c]==0:
            return 0
        if (r,c) in visited:
            return 0
        visited.add((r,c))

        return (1+dfs(r-1,c)+
        dfs(r+1,c)+
        dfs(r,c+1)+
        dfs(r,c-1))
    for i in range(rows):
        for j in range(col):
            if grid[i][j]==1 and (i,j) not in visited:
                x=dfs(i,j)
                mxarea=max(mxarea,x)
    return mxarea

mt=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(mt))
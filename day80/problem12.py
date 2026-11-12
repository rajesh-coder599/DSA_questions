# 1254. Number of Closed Islands




def closedIsland(grid):
    n=len(grid)
    m=len(grid[0])
    visited=set()
    def dfs(r,c):
        if not(0<=r<n and 0<=c<m):
            return False
        if grid[r][c]==1 or (r,c) in visited:
            return True
        visited.add((r,c))
        right=dfs(r+1,c)
        up=dfs(r,c+1)
        left=dfs(r-1,c)
        down=dfs(r,c-1)
        return right and left and up and down
    closed_island=0
    for i in range(n):
        for j in range(m):
            if (i,j) not in visited and grid[i][j]==0:
                if dfs(i,j):
                    closed_island+=1
    return closed_island
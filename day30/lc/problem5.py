# 463. Island Perimeter


def islandPerimeter(grid):
    rows=len(grid)
    col=len(grid[0])
    perameter=0

    for i in range(rows):
        for j in range(col):
            if grid[i][j]==1:
                perameter+=4
            if j<col-1 and grid[i][j+1]==1:
                perameter-=1
            if i<rows-1 and grid[i+1][j]==1:
                perameter-=1
    if perameter>4 :
        return perameter-1
    return perameter
mat=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(mat))

# with dfs
def islandPerimeter(grid):
    rows=len(grid)
    col=len(grid[0])
    visited=set()
    def dfs(i,j):
        if i<0 or j<0 or i>=rows or j>=col :
            return 1
        if grid[i][j]==0:
            return 1
        if (i,j) in visited:
            return 0
        visited.add((i,j))

        return (dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))
    for r in range(rows):
        for c in range(col):
            if grid[r][c]==1:
                return dfs(r,c)
# 200. Number of Islands


def numIslands(grid):
    rows=len(grid)
    col=len(grid[0])
    lands=0
    visited=set()
    def dfs(r,c):
        if r<0 or c<0 or r>=rows or c>=col :
            return
        if grid[r][c]=="0":
            return
        if (r,c) in visited:
            return
        visited.add((r,c))
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
        
    for i in range(rows):
        for j in range(col):
            if grid[i][j]=="1" and  (i,j) not in visited:
                lands+=1
                dfs(i,j)

    return lands
g=[
  ["1","1","0","1","0"],
  ["1","1","1","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(g))
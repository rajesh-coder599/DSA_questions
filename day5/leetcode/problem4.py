# 64. minimum path sum

grid=[[1,2,3],[4,5,6]]
m=len(grid)
n=len(grid[0])
def minpathsum(i,j,m,n,grid,dp):
    if i==m-1 and j==n-1:
        return grid[i][j]
    if i>=m or j>=n:
        return float("inf")
    if dp[i][j] != -1 :
        return dp[i][j]
    right=grid[i][j]+minpathsum(i+1,j,m,n,grid,dp)
    down=grid[i][j]+minpathsum(i,j+1,m,n,grid,dp)
    dp[i][j]=min(right,down)
    return dp[i][j]

dp=[[-1]*n ]*m
print(minpathsum(0,0,m,n,grid,dp))
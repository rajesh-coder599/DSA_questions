# 63. unique path part 2

grid=[[0,0,0],[0,1,0],[0,0,0]]

def uniquepath(i,j,grid,dp):
    if i==len(grid)-1 and j==len(grid[0])-1 and grid[i][j]!=1:
        return 1
    if i>=len(grid) or j>=len(grid[0]) or grid[i][j]==1:
        return 0
    if dp[i][j] != -1 :
        return dp[i][j]
    right=uniquepath(i+1,j,grid,dp)
    left=uniquepath(i,j+1,grid,dp)
    dp[i][j]=right+left

    return dp[i][j]

dp=[[-1 for _ in range((len(grid)))] for _ in range(len(grid[0]))]
print(uniquepath(0,0,grid,dp))
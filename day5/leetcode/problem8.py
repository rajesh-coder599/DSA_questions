# 3742. maximum path score in grid

grid=[[0,1],[2,0]]
k=1
def totalscore(i,j,grid,k,dp):

    if i>=len(grid) or j>=len(grid[0]):
        return -1

    cost=0
    if grid[i][j]>0 :
        cost=1
    k-=cost
    if k<0:
        return-1
    
    if i==len(grid)-1 and j==len(grid[0])-1 :
        return grid[i][j]

    if dp[i][j] != -1 :
        return dp[i][j]

    right=grid[i][j]+totalscore(i+1,j,grid,k,dp)
    down=grid[i][j]+totalscore(i,j+1,grid,k,dp)

    dp[i][j]=max(right,down)

    if dp[i][j]==-1:
        return -1
    return dp[i][j]

dp=[[-1 for _ in range(len(grid))] for _ in range(len(grid[0]))]
print(totalscore(0,0,grid,k,dp))
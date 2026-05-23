# biweekly contest 183
# Q3. Maximum Path Intersection Sum in a Grid


def maxScore(i,j,grid):
    n=len(grid)
    m=len(grid[0])
    if i==n-1:
        return grid[i][j]
    if j==0:
        return grid[i][j]

    first=grid[i][j]+maxScore(i+1,j,grid)
    fourth=grid[i][j]+maxScore(i,j-1,grid)

    return max(first,fourth)

grid = [[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]
print(maxScore(0,len(grid[0])-1,grid))
# 3619. Count Islands With Total Value Divisible by K



def countIslands(grid,k):
    n=len(grid)
    m=len(grid[0])
    vis=set()
    islands=[]
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    def dfs(r,c):
        if r<0 or c<0 or r>=n or c>=m or (r,c) in vis:
            return 0
        currsum=grid[r][c]
        vis.add((r,c))
        for x,y in direction:
            nr=r+x
            nc=c+y
            if 0<=nr<n and 0<=nc<m and  grid[nr][nc] != 0:
                currsum+=dfs(nr,nc)
        return currsum
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and (i,j) not in vis:
                temp=dfs(i,j)
                islands.append(temp)
    ans=0
    for i in islands:
        if i%k==0:
            ans+=1
    return ans

grid=[[3,0,3,0],[0,3,0,3],[3,0,3,0]]
k=3
print(countIslands(grid,k))
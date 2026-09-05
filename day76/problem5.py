# 1020. Number of Enclaves



def numEnclaves(grid):
    from collections import deque
    n=len(grid)
    m=len(grid[0])
    ans=0
    vis=set()
    def bfs(r,c):
        temp=1
        q=deque([(r,c)])
        vis.add((r,c))
        while q:
            i,j=q.popleft()
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)] :
                nr=i+x
                nc=j+y
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in vis and grid[nr][nc]==1:
                    q.append((nr,nc))
                    vis.add((nr,nc))
                    temp+=1
        return temp
    for c in range(m):
        if grid[0][c]==1 and (0,c) not in vis:
            bfs(0,c)
        if grid[n-1][c]==1 and (n-1,c) not in vis:
            bfs(n-1,c)
    for r in range(n):
        if grid[r][0]==1 and (r,0) not in vis:
            bfs(r,0)
        if grid[r][m-1]==1 and (r,m-1) not in vis:
            bfs(r,m-1)
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and (i,j) not in vis:
                temp=bfs(i,j)
                ans+=temp
    return ans
# 934. Shortest Bridge

from collections import deque
def shortestBridge(grid):
    n=len(grid)
    q=deque()
    vis=set()
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    def dfs(r,c):
        if grid[r][c]!=1 or (r,c) in vis:
            return
        q.append((r,c))
        vis.add((r,c))
        for x,y in direction:
            nr=r+x
            nc=c+y
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in vis :
                dfs(nr,nc)
    check=False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i,j)
                check=True
                break
        if check:
            break
    mndist=0
    while q:
        l=len(q)
        for _ in range(l):
            r,c=q.popleft()
            for x,y in direction:
                nr=r+x
                nc=c+y
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in vis :
                    if grid[nr][nc]==1:
                        return mndist
                    q.append((nr,nc))
                    vis.add((nr,nc))
        mndist+=1
            
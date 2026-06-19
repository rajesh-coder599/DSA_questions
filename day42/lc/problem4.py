# 934. Shortest Bridge

from collections import deque
def shortestBridge(grid):
    n=len(grid)
    q=deque()
    vis=set()
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                for x,y in direction:
                    ni=i+x
                    nj=j+y
                    if 0<=ni<n and 0<=nj<n and grid[ni][nj]==0:
                        q.append((ni,nj))
                        vis.add((ni,nj))
    mndist=0
    while q:
        mndist+=1
        l=len(q)
        for _ in range(l):
            r,c=q.popleft()
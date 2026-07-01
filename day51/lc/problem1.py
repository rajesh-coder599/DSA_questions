# 2812. Find the Safest Path in a Grid


from collections import deque
import heapq
def maximumSafenessFactor(grid):
    n=len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return 0
    thiefs=deque()
    vis=set()
    direction=[(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                thiefs.append((i,j))
                vis.add((i,j))
    while thiefs:
        r,c=thiefs.popleft()
        for x,y in direction :
            nr=x+r
            nc=y+c
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in vis:
                vis.add((nr,nc))
                grid[nr][nc]=grid[r][c]+1
                thiefs.append((nr,nc))
    hq=[]
    heapq.heappush(hq,(-grid[0][0],0,0))
    seen=set()
    while hq:
        safe,r,c=heapq.heappop()
        if (r,c) in seen:
            continue
        seen.add((r,c))
        safe=-safe
        if r==n-1 and c==n-1:
            return safe
        for x,y in direction:
            nr=x+r
            nc=y+c
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in seen:
                ns=min(safe,grid[nr][nc])
                heapq.heappush(-ns,nr,nc)
    
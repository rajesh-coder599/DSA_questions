# 994. Rotting Oranges

from collections import deque
def orangesRotting(grid):
    n=len(grid)
    m=len(grid[0])
    q=deque()
    seen=set()
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                q.append((i,j))
                seen.add((i,j))
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    time=0
    while q:
        check=False
        l=len(q)
        for _ in range(l):
            r,c=q.popleft()
            for x,y in directions:
                nr=r+x
                nc=c+y
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in seen and grid[nr][nc]==1:
                    q.append((nr,nc))
                    seen.add((nr,nc))
                    grid[nr][nc]=2
                    check=True
        if check:
            time+=1
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                return -1
    return time
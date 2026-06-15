# 1765. Map of Highest Peak

from collections import deque
def highestPeak(isWater):
    n=len(isWater)
    m=len(isWater[0])
    q=deque()
    visited=set()
    for i in range(n):
        for j in range(m):
            if isWater[i][j]==1:
                q.append((i,j))
                isWater[i][j]=0
                visited.add((i,j))
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    while q:
        l=len(q)
        for _ in range(l):
            r,c=q.popleft()
            for x,y in directions:
                nr=r+x
                nc=c+y
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc))
                    isWater[nr][nc]=isWater[r][c]+1
    return isWater
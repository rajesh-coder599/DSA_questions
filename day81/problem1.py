# 3882. Minimum XOR Path in a Grid



def minCost(grid):
    n=len(grid)
    m=len(grid[0])
    from collections import deque
    q=deque([(0,0,grid[0][0])])
    ans=1024
    visited={(0,0,grid[0][0])}
    while q:
        r,c,s=q.popleft()
        if r==n-1 and c==m-1:
            ans=min(ans,s)
            continue
        for x,y in [(1,0),(0,1)]:
            nr=x+r
            nc=y+c
            if 0<=nr<n and 0<=nc<m and (nr,nc,s^grid[nr][nc]) not in visited:
                q.append((nr,nc,s^grid[nr][nc]))
                visited.add((nr,nc,s^grid[nr][nc]))
    return ans
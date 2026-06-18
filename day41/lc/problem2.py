# 542. 01 Matrix

from collections import deque
def updateMatrix(mat):
    n=len(mat)
    m=len(mat[0])
    ans=[[-1 for _ in range(m)] for _ in range(n)]
    q=deque()
    seen=set()
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0:
                ans[i][j]=0
                q.append((i,j))
                seen.add((i,j))
    directions=[(1,0),(0,1),(0,-1),(-1,0)]
    while q:
        l=len(q)
        for _ in range(l):
            r,c=q.popleft()
            for x,y in directions:
                nr=r+x
                nc=c+y
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in seen :
                    seen.add((nr,nc))
                    ans[nr][nc]=ans[r][c]+1
                    q.append((nr,nc))
    return ans
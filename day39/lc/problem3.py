# 417. Pacific Atlantic Water Flow


from collections import deque
def pacificAtlantic(heights):
    n=len(heights)
    m=len(heights[0])
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    Atlantic=set()
    Pacific=set()
    def at(r,c):
        if (r,c) in Atlantic:
            return
        Atlantic.add((r,c))
        for i,j in directions:
            nr=r+i
            nc=c+j
            if 0<=nr<n and 0<=nc<m and (nr,nc) not in Atlantic and heights[nr][nc]>=heights[r][c] :
                at(nr,nc)
    def pac(r,c):
        if (r,c) in Pacific:
            return
        Pacific.add((r,c))
        for i,j in directions:
            nr=r+i
            nc=c+j
            if 0<=nr<n and 0<=nc<m and (nr,nc) not in Pacific and heights[nr][nc]>=heights[r][c] :
                pac(nr,nc)
    ## right
    for i in range(n):
        at(i,m-1)
    ## botom
    for i in range(m):
        at(n-1,i)
    ## left
    for j in range(n):
        pac(j,0)
    ## top
    for j in range(m):
        pac(0,j)
    ans=[]
    for i in range(n):
        for j in range(m):
            if (i,j) in Atlantic and (i,j) in Pacific:
                ans.append([i,j])
    return ans
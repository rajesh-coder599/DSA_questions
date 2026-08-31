# 959. Regions Cut By Slashes



def regionsBySlashes(grid):
    from collections import deque
    n=len(grid)
    mat=[]
    arr=[]
    nxtrow=[]
    third=[]
    for i in grid:
        for j in i:
            if j==" ":
                arr.append(0)
                arr.append(0)
                arr.append(0)
                nxtrow.append(0)
                nxtrow.append(0)
                nxtrow.append(0)
                third.append(0)
                third.append(0)
                third.append(0)
            elif j=="/":
                arr.append(0)
                arr.append(0)
                arr.append(1)
                nxtrow.append(0)
                nxtrow.append(1)
                nxtrow.append(0)
                third.append(1)
                third.append(0)
                third.append(0)
            else:
                arr.append(1)
                arr.append(0)
                arr.append(0)
                nxtrow.append(0)
                nxtrow.append(1)
                nxtrow.append(0)
                third.append(0)
                third.append(0)
                third.append(1)
        mat.append(arr)
        mat.append(nxtrow)
        mat.append(third)
        third=[]
        arr=[]
        nxtrow=[]
    vis=set()
    def bfs(r,c):
        q=deque()
        q.append((r,c))
        while q:
            x,y=q.popleft()
            if (x,y) in vis:
                continue
            vis.add((x,y))
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)] :
                nr=x+a
                nc=y+b
                if 0<=nr<3*n and 0<=nc<3*n and mat[nr][nc]==0 and (nr,nc) not in vis:
                    q.append((nr,nc))
    ans=0
    for r in range(3*n):
        for c in range(3*n):
            if mat[r][c]==0 and (r,c) not in vis:
                ans+=1
                bfs(r,c)
    return ans
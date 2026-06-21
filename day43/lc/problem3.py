# 3568. Minimum Moves to Clean the Classroom


## tried but did not got an a solution
from collections import deque
def minMoves(classroom,energy):
    n=len(classroom)
    m=len(classroom[0])
    q=deque()
    vis=set()
    litter=0
    for i in range(n):
        for j in range(m):
            if classroom[i][j]=="S" :
                q.append((i,j,energy))
                vis.add((i,j))
            if classroom[i][j]=="L" :
                litter+=1
    direction=[(0,1),(1,0),(-1,0),(0,-1)]
    mnmoves=0
    while q:
        l=len(q)
        for _ in range(l):
            r,c,k=q.popleft()
            for x,y in direction:
                nr=r+x
                nc=c+y
                nk=k-1
                if 0<=nr<n and 0<=nc<m and classroom[nr][nc] != "X" and (nr,nc) not in vis :
                    if nk==0 and classroom[nr][nc] != "R" :
                        continue
                    if classroom[nr][nc]=="R":
                        nk=energy
                        q.append((nr,nc,nk))
                        vis.add((nr,nc))
                    elif classroom[nr][nc]=="." :
                        q.append((nr,nc,nk))
                        vis.add((nr,nc))
                    else:
                        litter-=1
                        q.append((nr,nc,nk))
                        vis.add((nr,nc))
        mnmoves+=1
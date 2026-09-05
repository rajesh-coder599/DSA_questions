# 3568. Minimum Moves to Clean the Classroom



def minMoves(classroom,energy):
    from collections import deque
    n=len(classroom)
    m=len(classroom[0])
    a=None
    b=None
    litter_count=0
    litter_id={}
    for i in range(n):
        for j in range(m):
            if classroom[i][j]=="S":
                a=i
                b=j
            if classroom[i][j]=="L":
                litter_id[(i,j)]=litter_count
                litter_count+=1
    if litter_count==0:
        return 0
    collected_litter=0
    target=(1<<litter_count)-1
    q=deque()
    q.append((a,b,energy,collected_litter,0))
    vis=set()
    vis.add((a,b,energy,collected_litter))
    while q:
        r,c,e,cl,s=q.popleft()
        if cl==target:
            return s
        if e==0:
            continue
        for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr=r+x
            nc=c+y
            if nr<0 or nr>=n or nc<0 or nc>=m:
                continue
            if classroom[nr][nc]=="X":
                continue
            ne=e-1
            ncl=cl
            if classroom[nr][nc]=="L":
                id=litter_id[(nr,nc)]
                ncl=ncl | (1<<id)
            elif classroom[nr][nc]=="R":
                ne=energy
            state=(nr,nc,ne,ncl)
            if state not in vis:
                vis.add(state)
                q.append((nr,nc,ne,ncl,s+1))
    return -1
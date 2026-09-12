# 4046. Minimum Cost Path With At Most K Turns


## WA by this method
def minCost(grid,k):
    from collections import deque
    n=len(grid)
    m=len(grid[0])
    vis=set()
    q=deque([(0,0,k," ",grid[0][0])])
    vis.add((0,0,grid[0][0],k))
    ans=float("inf")
    while q:
        r,c,turns,dire,cost=q.popleft()
        for x,y,nd in [(1,0,"D"),(0,1,"R"),(-1,0,"U"),(0,-1,"L")]:
            nr=r+x
            nc=c+y
            if 0<=nr<n and 0<=nc<m and (nr,nc,cost+grid[nr][nc],turns) not in vis:
                nt=turns
                if dire!=" " and nd!=dire:
                    nt-=1
                if nt<0:
                    continue
                ncost=cost+grid[nr][nc]
                if (nr,nc)==(n-1,m-1):
                    ans=min(ans,ncost)
                vis.add((nr,nc,ncost,nt))
                q.append((nr,nc,nt,nd,ncost))
    if ans==float("inf"):
        return -1
    return ans

## by dijskart

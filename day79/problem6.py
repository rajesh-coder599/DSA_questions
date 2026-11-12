# 4084. Last Visited Cell in a Directional Grid



def lastVisitedCell(grid):
    n=len(grid)
    m=len(grid[0])
    visited={(0,0)}
    r=0
    c=0
    while True:
        nr=r
        nc=c
        if grid[r][c]=="R":
            nc+=1
        elif grid[r][c]=="L":
            nc-=1
        elif grid[r][c]=="U":
            nr-=1
        else:
            nr+=1
        if (nr,nc) in visited or not(0<=nr<n and 0<=nc<m):
            return [r,c]
        r=nr
        c=nc
        visited.add(nr,nc)

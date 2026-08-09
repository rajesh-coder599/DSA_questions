# 1140. Stone Game II


## WA (am dumb coder)
def stoneGameII(piles):
    n=len(piles)
    vis=set()
    def mxstones(m,a,turn):
        alise=0
        bob=0
        for x in range(2*m+a):
            if x in vis:
                continue
            if x>=n:
                break
            vis.add(x)
            if turn==0:
                alise=max(alise,piles[x]+mxstones(max(m,x),a+1,1))
            else:
                bob=max(bob,piles[x]+mxstones(max(m,x),a+1,0))
        return alise
    return mxstones(1,0)
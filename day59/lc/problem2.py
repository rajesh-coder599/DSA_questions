# 4003. Minimum Cost Path with Alternating Directions III



def minCost(m,n,penalty):
    import heapq
    dp=[[[float("inf")]*2 for _ in range(n)] for _ in range(m)]
    h=[]
    heapq.heappush(h,(-1,0,0,1))
    dp[0][0][1]=1
    vis=set()
    while heapq:
        _,i,j,p=heapq.heappop(h)
        if (i,j,p) in vis:
            continue
        vis.add((i,j,p))

        if dp[i][j][1-p]>dp[i][j][p]+penalty[i][j] :
            dp[i][j][1-p]=dp[i][j][p]+penalty[i][j]
            heapq.heappush(h,(-dp[i][j][1-p],i,j,1-p))

        for x,y in [(1,0),(0,1)] :
            ni=x+i
            nj=y+j
            if 0<=ni<m and 0<=nj<n :
                cost=(ni+1)*(nj+1)+dp[i][j][p]+(penalty[i][j] if p==0 else 0)
                if dp[ni][nj][1-p]>cost:
                    dp[ni][nj][1-p]=cost
                    heapq.heappush(h,(-dp[ni][nj][1-p],ni,nj,1-p))
        for x,y in [(-1,0),(0,-1)] :
            ni=x+i
            nj=y+j
            if 0<=ni<m and 0<=nj<n :
                cost=cost=(ni+1)*(nj+1)+dp[i][j][p]+(penalty[i][j] if p==1 else 0)
                if dp[ni][nj][1-p]>cost:
                    dp[ni][nj][1-p]=cost
                    heapq.heappush(h,(-dp[ni][nj][1-p],ni,nj,1-p))

    return min(dp[m-1][n-1][1],dp[m-1][n-1],[0])
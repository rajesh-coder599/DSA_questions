# 3665. Twisted Mirror Path Count



def uniquePaths(grid):
    mod=1000000007
    n=len(grid)
    m=len(grid[0])
    memo={}
    def rec(r,c,prev):
        if r>=n or c>=m:
            return 0
        if r==n-1 and c==m-1:
            return 1
        if (r,c) in memo:
            return memo[(r,c)]
        if grid[r][c]==1:
            if prev==0:
                return rec(r+1,c,1)
            else:
                return rec(r,c+1,0)
        ans=0
        ans=(ans+rec(r+1,c,1))%mod
        ans=(ans+rec(r,c+1,0))%mod
        memo[(r,c)]=ans
        return memo[(r,c)]
    return rec(0,0,-1)
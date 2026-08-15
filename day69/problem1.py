# 279. Perfect Squares



def numSquares(n):
    dp=[-1]*(n+1)
    def mnsqrs(n):
        if n<=0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        j=1
        ans=float("inf")
        while j*j<=n:
            ans=min(ans,1+mnsqrs(n-j*j))
            j+=1
        dp[n]=ans
        return dp[n]
    return mnsqrs(n)
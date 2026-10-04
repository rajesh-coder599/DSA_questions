# 4050. Minimum Days to Score Exactly N Points





def minDays(n):
    memo=[-1]*(n+1)
    def solve(x):
        if x==0:
            return 0
        if memo[x] != -1:
            return memo[x]
        ans=float("inf")
        k=1
        while k*(k+1)//2<x:
            point=k*(k+1)//2
            ans=min(ans,k+1+solve(x-point))
            k+=1
        memo[x]=ans
        return memo[x]
    return solve(n)
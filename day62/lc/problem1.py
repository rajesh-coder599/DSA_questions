# 1406. Stone Game III




def stoneGameIII(stoneValue):
    n=len(stoneValue)
    dp=[0]*(n+1)
    for i in range(n-1,-1,-1):
        diff=-float("inf")
        take=0
        for j in range(3):
            if i+j>=n:
                break
            take+=stoneValue[i+j]
            diff=max(diff,take-dp[i+j+1])
        dp[i]=diff
    if dp[0]>0:
        return "Alice"
    if dp[0]<0:
        return "Bob"
    return "Tie"
# 1872. Stone Game VIII



def stoneGameVIII(stones):
    prefix=[stones[0]]
    n=len(stones)
    for i in range(1,n):
        prefix.append(prefix[i-1]+stones[i])
    dp=prefix[-1]
    for i in range(n-2,0,-1):
        dp=max(dp,prefix[i]-dp)
    return dp
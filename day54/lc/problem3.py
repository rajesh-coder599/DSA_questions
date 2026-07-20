# 3995. Minimum Cost to Convert String III



def minCost(source,target,rules,costs):
    if len(source) != len(target) :
        return -1
    n=len(source)
    m=len(rules)
    dp=[float("inf")]*(n+1)
    dp[0]=0
    for i in range(n):
        if dp[i]==float("inf"):
            continue
        if source[i]==target[i]:
            dp[i+1]=min(dp[i],dp[i+1])
        for j in range(m):
            pat=rules[j][0]
            rep=rules[j][1]
            l=len(pat)
            cost=costs[j]
            check=True
            if l+i>n:
                continue
            for k in range(l):
                if target[i+k]!=rep[k] :
                    check=False
                    break
                if pat[k]=="*":
                    cost+=1
                elif source[k+i]!=pat[k]:
                    check=False
                    break
            if not check:
                continue
            dp[i+l]=min(dp[i+l],dp[i]+cost)
    if dp[-1]==float("inf"):
        return -1
    return dp[-1]
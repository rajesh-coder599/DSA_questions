# 746. Min Cost Climbing Stairs

cost = [1,100,1,1,1,100,1,1,100,1]
n=len(cost)
# recursion
def rec(cost,i):
        if i>=len(cost):
            return 0
        one_step=cost[i]+rec(cost,i+1)
        two_step=cost[i]+rec(cost,i+2)
        return min(one_step,two_step)

print(min(rec(cost,0),rec(cost,1)))

# memorization
def memo(cost,i,dp):
        if i>=len(cost):
            return 0
        if dp[i] != -1 :
              return dp[i]
        one_step=cost[i]+memo(cost,i+1,dp)
        two_step=cost[i]+memo(cost,i+2,dp)
        dp[i] = min(one_step,two_step)
        return dp[i]

dp=[-1]*n
print(min(memo(cost,0,dp),memo(cost,1,dp)))

# tabulation
def tab(cost):
        n=len(cost)
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=0
        for i in range(2,n+1):
              dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]
        

print(tab(cost))

# tabulation with space optimization
def so(cost):
        n=len(cost)
        a=0
        b=0
        for i in range(2,n+1):
              c=min(b+cost[i-1],a+cost[i-2])
              a=b
              b=c
        return b
        

print(so(cost))
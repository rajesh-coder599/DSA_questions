# 4009. Minimum Possible Maximum Waiting Time



def minMaxWaitingTime(demand,fuel):
    n=len(demand)
    memo={}
    def mx_car(i,f0,f1):
        if i>=n:
            return 0
        state=(i,f0,f1)
        if state in memo:
            return memo[state]
        ans=0
        curr_demand=demand[i]
        if curr_demand<=f0:
            ans=max(ans,1+mx_car(i+1,f0-curr_demand,f1))
        if curr_demand<=f1:
            ans=max(ans,1+mx_car(i+1,f0,f1-curr_demand))
        memo[state]=ans
        return ans
    max_car=mx_car(0,fuel[0],fuel[1])
    if max_car==0:
        return -1
    def minmax_wait(i,f0,f1,t0,t1,max_wait,target_cars):
        if i==target_cars:
            return True
        state=(i,f0,f1,t0,t1)
        if state in memo:
            return memo[state]
        curr_demand=demand[i]
        if curr_demand<=f0:
            if t0<=max_wait:
                if minmax_wait(i+1,f0-curr_demand,f1,curr_demand,max(0,t1-t0),max_wait,target_cars):
                    memo[state]=True
                    return True
        if curr_demand<=f1:
            if t1<=max_wait:
                if minmax_wait(i+1,f0,f1-curr_demand,max(0,t0-t1),curr_demand,max_wait,target_cars):
                    memo[state]=True
                    return True
        memo[state]=False
        return False
    l=0
    r=sum(demand)
    ans=r
    while l<=r:
        memo.clear()
        mid=(l+r)//2
        if minmax_wait(0,fuel[0],fuel[1],0,0,mid,max_car):
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans


demand = [6,8,4,6,5]
fuel = [16,13]
print(minMaxWaitingTime(demand,fuel))
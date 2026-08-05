# 4009. Minimum Possible Maximum Waiting Time


## wrong code i will update it latter

def minMaxWaitingTime(demand,fuel):
    n=len(demand)
    prefix_sum=[0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1]+demand[i])
    total_fuel0,total_fuel1=fuel[0],fuel[1]
    memo={}
    def can_serve(i,f0,diff,max_wait,target_cars):

        if i==target_cars:
            return True
        state=(i,f0,diff,max_wait,target_cars)
        if state in memo:
            return memo[state]
        curr_demand=demand[i]

        sum_of_demand=prefix_sum[i]
        used_f0=total_fuel0-f0
        used_f1=sum_of_demand-used_f0
        f1=total_fuel1-used_f1

        if f0>=curr_demand:
            wait0=max(0,diff)
            if wait0<=max_wait:
                next_diff=diff+curr_demand
                if can_serve(i+1,f0-curr_demand,next_diff,max_wait,target_cars):
                    memo[state]=True
                    return True

        if f1>=curr_demand:
            wait1=max(0,-diff)
            if wait1<=max_wait:
                next_diff=diff-curr_demand
                if can_serve(i+1,f0,next_diff,max_wait,target_cars):
                    memo[state]=True
                    return True

        memo[state]=False
        return False

    max_car=0
    memo.clear()
    for i in range(n,0,-1):
        if can_serve(0,total_fuel0,0,float("inf"),i):
            max_car=i
            break

    if max_car==0:
        return -1

    low=0
    high=sum(demand)
    ans=high

    while low<=high:
        mid=(low+high)//2
        memo.clear()
        if can_serve(0,total_fuel0,0,mid,max_car):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
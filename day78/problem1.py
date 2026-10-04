# 3414. Maximum Score of Non-overlapping Intervals




def maximumWeight(intervals):
    n=len(intervals)
    new_intervals=[]
    for i in range(n):
        l,r,w=intervals[i]
        new_intervals.append((l,r,w,i))
    new_intervals.sort()
    def bs(target):
        l=0
        r=n-1
        ans=n
        while l<=r:
            mid=(l+r)//2
            if new_intervals[mid][0]<=target:
                l=mid+1
            else:
                r=mid-1
                ans=mid
        return ans
    memo={}
    def solve(i,k):
        if i>=n or k==0:
            return (0,[])
        if (i,k) in memo:
            return memo[(i,k)]
        l,r,w,orignal_idx=new_intervals[i]
        idx=bs(r)
        take_score,take_arr=solve(idx,k-1)
        take_score+=w
        take_arr=[orignal_idx]+take_arr
        take_arr.sort()
        not_take_score,not_take_arr=solve(i+1,k)
        if take_score<not_take_score:
            ans=(not_take_score,not_take_arr)
        elif take_score>not_take_score:
            ans=(take_score,take_arr)
        else:
            ans=min((take_score,take_arr),(not_take_score,not_take_arr),key=lambda x: x[1])
        memo[(i,k)]=ans
        return ans
    return solve(0,4)[1]


a=[[12,15,7],[1,13,44],[11,22,28],[6,12,5],[12,23,42],[11,19,49],[16,23,50],[18,21,16],[2,14,6],[4,16,12]]
print(maximumWeight(a))
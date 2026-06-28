# 3976. Maximum Subarray Sum After Multiplier

## WA
import math
def maxSubarraySum(nums,k):
    if max(nums)<=0:
        return math.ceil(max(nums)/k)
    n=len(nums)
    mxsum=[0,0,0]
    currsum=[0,-1]
    for i in range(n):
        if currsum[1]==-1:
            currsum[1]=i
        currsum[0]+=nums[i]
        if mxsum[0]<currsum[0]:
            mxsum=[currsum[0],currsum[1],i]
        elif currsum[0]<0:
            currsum=[0,-1]
    x=mxsum[1]
    y=mxsum[2]
    arr=nums[x:y+1]
    a=0
    b=0
    for i in arr:
        a+=i*k
    for i in arr:
        b+=math.ceil(i/k)
    return max(a,b)
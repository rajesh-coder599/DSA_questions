# 2574. Left and Right Sum Differences


def leftRightDifference(nums):
    n=len(nums)
    perfixsum=[nums[0]]
    sufixsum=[0]*n
    sufixsum[n-1]=nums[n-1]
    for i in range(1,n):
        perfixsum.append(perfixsum[i-1]+nums[i])
    for i in range(n-2,-1,-1):
        sufixsum[i]=sufixsum[i+1]+nums[i]
    ans=[]
    for i in range(n):
        ans.append(abs(perfixsum[i]-sufixsum[i]))
    return ans
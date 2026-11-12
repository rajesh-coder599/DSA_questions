# 4097. Minimum Value of Merged Integers




def minMergedInteger(nums):
    ans=float("inf")
    n=len(nums)
    for i in range(0,n,2):
        temp=str(nums[i])+str(nums[i+1])
        ans=min(ans,int(temp))
    return ans
# 4054. Count Shadow Pairs I




def shadowPairs(nums):
    n=len(nums)
    mn=nums[0]
    mn_count=1
    ans=0
    for i in range(1,n):
        if nums[i]<mn:
            mn=nums[i]
            mn_count=1
        elif nums[i]==mn:
            mn_count+=1
        else:
            ans+=mn_count
    return ans
# 53. maximum subarry

nums=[-2,1,-3,4,-1,2,1,-5,4]
def maxsum(nums):
    
    curr=nums[0]
    best=nums[0]
    for i in range(1,len(nums)):
        curr=max(nums[i],curr+nums[i])
        best=max(best,curr)

    return best

print(maxsum(nums))
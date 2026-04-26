# 3914. Minimum Operations to Make Array Non Decreasing

def minOperations(nums):
    n=len(nums)
    a=0
    for i in range(n-1,0,-1):
        if nums[i]<nums[i-1]:
            a+=nums[i-1]-nums[i]
    return a

nums=[3,3,2,1]
print(minOperations(nums))
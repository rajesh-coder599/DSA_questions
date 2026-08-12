# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum



def missingInteger(nums):
    n=len(nums)
    num=nums[i]+1
    for i in range(1,n):
        if nums[i]==nums[i-1]+1:
            num=nums[i]+1
        else:
            break
    a=set(nums)
    while num in a:
        num+=1
    return num
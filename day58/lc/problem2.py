# 628. Maximum Product of Three Numbers



def maximumProduct(nums):
    nums.sort()
    a=nums[-1]*nums[-2]*nums[-3]
    if nums[0]<0 and nums[1]<0:
        temp=nums[0]*nums[1]*nums[-1]
        a=max(a,temp)
    return a
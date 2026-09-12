# 4044. Count Good Cyclic Rotations





def countGoodRotations(nums):
    n=len(nums)
    first_half=sum(nums[:n//2])
    second_half=sum(nums[n//2:])
    ans=0
    for i in range(n):
        if first_half>second_half:
            ans+=1
        first_half-=nums[i]
        second_half+=nums[i]
        first_half+=nums[(i+n//2)%n]
        second_half-=nums[(i+n//2)%n]
    return ans
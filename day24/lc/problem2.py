# biweekly contest 183
# Q1. Minimum Swaps to Move Zeros to End


def minimumSwaps(nums):
    n=len(nums)
    zeros=0
    for i in nums:
        if i==0:
            zeros+=1
    ans=0
    ind=n-1
    while zeros>0:
        if nums[ind]==0:
            zeros-=1
        else:
            zeros-=1
            ans+=1
        ind-=1
    return ans

nums=[0,1,0,3,12]
print(minimumSwaps(nums))
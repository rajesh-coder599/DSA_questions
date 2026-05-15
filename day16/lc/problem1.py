# 153. Find Minimum in Rotated Sorted Array

def findMin(nums):
    n=len(nums)
    l=0
    r=n-1
    ans=None
    while l<r:
        mid=(l+r)//2
        a=nums[mid]
        if a>nums[r]:
            l=mid+1
        else:
            r=mid

    return nums[r]


nums=[4,5,6,7,8,9,10,0,1,2]
print(findMin(nums))
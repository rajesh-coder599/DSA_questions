# 33. Search in Rotated Sorted Array


def search(nums,target):
    n=len(nums)
    if nums[n-1]==target:
        return n-1
    if nums[0]==target:
        return 0
    
    l=0
    r=n-1
    ans=None
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            ans=mid
            break
        if nums[mid]<target:
            
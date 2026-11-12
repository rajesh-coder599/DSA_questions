# 34. Find First and Last Position of Element in Sorted Array



def searchRange(nums,target):
    n=len(nums)
    l=0
    r=n-1
    while l<r:
        mid=(l+r)//2
        if nums[mid]<target:
            l=mid+1
        else:
            r=mid
    first=l
    if nums[first]!=target:
        return [-1,-1]
    l=0
    r=n-1
    while l<r:
        mid=(l+r)//2
        if nums[mid]<=target:
            l=mid+1
        else:
            r=mid
    if nums[r]==target:
        last=r
    else:
        last=l-1
    return [first,last]
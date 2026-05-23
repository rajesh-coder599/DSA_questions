# 1752. Check if Array Is Sorted and Rotated


def check(nums):
    n=len(nums)
    if n==1:
        return True
    check=False
    for i in range(n):
        if nums[i]>nums[(i+1)%n]:
            if check:
                return False
            check=True
    
    return True

nums = [2,1,3,4]
print(check(nums))
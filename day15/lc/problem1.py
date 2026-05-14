# 2784. Check if Array is Good


nums = [1, 1]
def isGood(nums):
    n=len(nums)
    a=set(nums)
    for i in range(1,n):
        if i not in a:
            return False
    if nums.count(n-1)==2:
        return True
    return False
print(isGood(nums))
        
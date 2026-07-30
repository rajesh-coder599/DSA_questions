# 1464. Maximum Product of Two Elements in an Array



def maxProduct(nums):
    nums.sort()
    return (nums[-1]-1)*(nums[-2]-1)
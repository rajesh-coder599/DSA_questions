# 3925. Concatenate Array With Reverse

def concatWithReverse(nums):
        a=nums.copy()
        a.reverse()
        nums=nums+a
        return nums

nums=[1,2,3]
print(concatWithReverse(nums))
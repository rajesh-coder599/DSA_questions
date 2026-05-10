# 396. rotate function

def maxrotatefunction(i,j,nums):
    if j==len(nums)-1:
        return nums[j]*i
    if j>=len(nums):
        return 0
    if i==len(nums)-1:
        return i
    if i>=len(nums):
        return 0
    rotate=nums[j]*i+maxrotatefunction(i,j+1,nums)
    multiply=nums[j]*i+maxrotatefunction(i+1,j,nums)    

    return max(rotate,multiply)

nums=[4,3,2,6]
print(maxrotatefunction(0,0,nums))
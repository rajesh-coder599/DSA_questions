# 4088. Difference Between Peaks and Valleys



def peakValleyDifference(nums):
    n=len(nums)
    p=0
    v=0
    for i in range(1,n-1):
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            p+=nums[i]
        if nums[i]<nums[i-1] and nums[i]<nums[i+1]:
            v+=nums[i]
    return p-v
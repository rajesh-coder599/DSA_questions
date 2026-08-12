# 41. First Missing Positive



def firstMissingPositive(nums):
    nums.sort()
    ans=1
    for i in nums:
        if i==ans:
            ans+=1
    return ans
# 3727. Maximum Alternating Sum of Squares



def maxAlternatingSum(nums):
    n=len(nums)
    for i in range(n):
        nums[i]*=nums[i]
    nums.sort(reverse=True)
    mxscore=0
    for i in range(n):
        if i<=(n+1)//2:
            mxscore+=nums[i]
        else:
            mxscore-=nums[i]
    return mxscore
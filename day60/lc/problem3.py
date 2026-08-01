# 486. Predict the Winner



def predictTheWinner(nums):
    n=len(nums)
    def dp(l,r):
        if l==r:
            return nums[l]
        left=nums[l]-dp(l+1,r)
        right=nums[r]-dp(l,r-1)
        return max(left,right)
    return dp(0,n-1)>=0
    
nums=[1,5,233,7]
print(predictTheWinner(nums))
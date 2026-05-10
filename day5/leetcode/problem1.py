# 55. jump game

nums=[2,3,1,1,0,4]
def isposible(i,nums,dp):
    if i>=len(nums)-1 :
        return True
    if dp[i]!=False:
        return dp[i]
    for j in range(1,nums[i]+1):
        
        if isposible(i+j,nums,dp):
            dp[i]=True
        
    return dp[i]


n=len(nums)
dp=[False]*n
print(isposible(0,nums,dp))


# 45. jump game part 2

nums=[2,3,1,1,4]

def minjump(i,nums):
    if i>=len(nums)-1:
        return 0
    ans=float("inf")
    for j in range(1,nums[i]+1):
        ans=min(ans,1+minjump(i+j,nums))


    return ans

print(minjump(0,nums))
# 3974. Maximum Total Sum of K Selected Elements


def maxSum(nums,k,mul):
    nums.sort(reverse=True)
    selectednums=[]
    for i in range(k):
        selectednums.append(nums[i])
    ans=0
    for i in selectednums:
        if mul>1:
            ans+=i*mul
        else:
            ans+=i
        mul-=1
    return ans
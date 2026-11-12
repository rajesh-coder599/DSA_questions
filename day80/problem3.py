# 3644. Maximum K to Sort a Permutation


def sortPermutation(nums):
    n=len(nums)
    ans=-1
    for i in range(n):
        val=nums[i]
        if i!=val:
            if ans==-1:
                ans=val
            else:
                ans&=val
    return ans
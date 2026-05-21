# 15. 3Sum


def threeSum(nums):
    n=len(nums)
    ans=[]
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    a=[nums[i],nums[j],nums[k]]
                    a.sort()
                    if a not in ans:
                        ans.append(a)
    return ans
nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))
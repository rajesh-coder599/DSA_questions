# 4099. Minimum Operations to Sort With Locked Indices




def minOperations(nums,locked,k):
    n=len(nums)
    ans=0
    for i in range(n):
        temp=0
        nk=0
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                temp+=1
                if locked[j]==1:
                    nk+=1
                    locked[j]=0
                if locked[j+1]==1:
                    nk+=1
                    locked[j+1]=0
        if nk>k:
            return -1
        k-=nk
        ans+=temp+nk
    return ans
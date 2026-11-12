# 4083. Minimum Deletions to Make Array Sharp




def minDeletions(nums):
    prev=nums[0]
    ans=0
    d=0
    for i in range(1,len(nums)):
        if prev==nums[i]:
            d+=1
        else:
            ans+=d
            d=0
            prev=nums[i]
    ans+=d
    return ans
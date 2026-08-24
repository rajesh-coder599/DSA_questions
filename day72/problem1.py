# 3471. Find the Largest Almost Missing Integer


def largestInteger(nums,k):
    if len(nums)==k:
        return max(nums)
    from collections import defaultdict
    freq=defaultdict(int)
    for i in nums:
        freq[i]+=1
    ans=-1
    if freq[nums[0]]==1:
        ans=max(ans,nums[0])
    if freq[nums[-1]]==1:
        ans=max(ans,nums[-1])
    if k==1:
        for k,v in freq.items():
            if v==1:
                ans=max(ans,k)
    return ans
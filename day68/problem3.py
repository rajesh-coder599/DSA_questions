# 2958. Length of Longest Subarray With at Most K Frequency




def maxSubarrayLength(nums,k):
    from collections import defaultdict
    n=len(nums)
    mxln=k
    freq=defaultdict(int)
    l=0
    r=0
    while r<n:
        temp=nums[r]
        freq[temp]+=1
        r+=1
        while freq[temp]>k:
            freq[nums[l]]-=1
            l+=1
        mxln=max(mxln,r-l+1)
    return mxln
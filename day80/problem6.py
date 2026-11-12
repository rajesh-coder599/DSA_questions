# 4089. Count Subarrays With Loose Bounds




def countSubarrays(nums,minK,maxK):
    ans=0
    curr_len=0
    for i in nums:
        if i>=minK and i<=maxK:
            curr_len+=1
            ans+=curr_len
        else:
            curr_len=0
    return ans
# 673. Number of Longest Increasing Subsequence


def findNumberOfLIS(nums):
    from collections import defaultdict
    n=len(nums)
    dp=[1]*n
    count=[1]*n
    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]:
                if dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    count[i]=count[j]
                elif dp[j]+1==dp[i]:
                    count[i]+=count[j]

    target=max(dp)
    ans=0
    for i in range(n):
        if target==dp[i]:
            ans+=count[i]
    return ans
# 3702. Longest Subsequence With Non-Zero Bitwise XOR



def longestSubsequence(nums):
    n=len(nums)
    if sum(nums)==0:
        return 0
    xor=0
    for num in nums:
        xor^=num
    if xor==0:
        return n-1
    return n
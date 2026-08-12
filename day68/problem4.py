# 395. Longest Substring with At Least K Repeating Characters


## brute force
def longestSubstring(s,k):
    from collections import defaultdict
    ans=-float("inf")
    n=len(s)
    for i in range(n):
        freq=defaultdict(int)
        ln=0
        for j in range(i,n):
            freq[s[j]]+=1
            ln+=1
            check=True
            for v in freq.values():
                if v<k:
                    check=False
                    break
            if check:
                ans=max(ans,ln)
    return ans
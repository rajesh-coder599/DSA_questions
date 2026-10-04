# 1520. Maximum Number of Non-Overlapping Substrings




def maxNumOfSubstrings(s):
    n=len(s)
    occurenc={}
    for i in range(n):
        if s[i] not in occurenc:
            occurenc[s[i]]=[i,i]
        else:
            occurenc[s[i]][1]=i
    ans=0
    last_idx=0
    for i in range(n):
        l,r=occurenc[s[i]]
        if r==i and l>=last_idx:
            ans+=1
            last_idx=r+1
    return ans

s = "adefaddaccc"
print(maxNumOfSubstrings(s))
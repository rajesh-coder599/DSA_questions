# 3090. Maximum Length Substring With Two Occurrences



def maximumLengthSubstring(s):
    from collections import defaultdict
    mxln=0
    freq=defaultdict(int)
    l=0
    n=len(s)
    for r in range(n):
        a=s[r]
        freq[a]+=1
        while freq[a]>2:
            freq[s[l]]-=1
            l+=1
        mxln=max(mxln,r-l+1)
    return mxln
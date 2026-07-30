# 3517. Smallest Palindromic Rearrangement I


def smallestPalindrome(s):
    from collections import defaultdict
    freq=defaultdict(int)
    a=set()
    for i in s:
        freq[i]+=1
        a.add(i)
    a=list(a)
    a.sort(reverse=True)
    n=len(s)
    ans=[-1]*n
    if n%2 != 0:
        ans[n//2]=s[n//2]
    for i in range(n//2):
        if freq[a[-1]]<2:
            a.pop()
        ans[i]=a[-1]
        ans[n-i-1]=a[-1]
        freq[a[-1]]-=2
        if freq[a[-1]]<2:
            a.pop()
    finalstr="".join(ans)
    return finalstr
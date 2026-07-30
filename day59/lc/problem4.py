# 3518. Smallest Palindromic Rearrangement II



def smallestPalindrome(s,k):
    from collections import defaultdict
    freq=defaultdict(int)
    a=set()
    for i in s:
        freq[i]+=1
        a.add(i)
    a=list(a)
    a.sort()
    n=len(s)
    halfstr=""
    for i in a:
        if freq[i]>1:
            x=i*freq[i]//2
            halfstr+=x
    if (len(halfstr)*(len(halfstr)-1))//2+1>k:
        return ""
    
    if n%2 != 0:
        halfstr+=s[n//2]
    
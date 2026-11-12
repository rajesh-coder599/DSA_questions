# 3863. Minimum Operations to Sort a String



def minOperations(s):
    n=len(s)
    if n==1:
        return 0
    mn=s[0]
    mx=s[0]
    mn_freq=1
    mx_freq=1
    check=True
    for i in range(1,n):
        char=s[i]
        if mn>char:
            mn=char
            mn_freq=1
        elif mn==char:
            mn_freq+=1
        if mx<char:
            mx=char
            mx_freq=1
        elif mx==char:
            mx_freq+=1
        if s[i-1]>s[i]:
            check=False
    if check:
        return 0
    if n==2:
        return -1
    if s[0]==mn or s[-1]==mx:
        return 1
    if s[0]==mx and s[-1]==mn:
        if mn_freq>1 or mx_freq>1:
            return 2
        return 3
    return 2
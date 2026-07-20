# 3993. Maximum Value of an Alternating Sequence



def maximumValue(n,s,m):
    if n==1:
        return s+1
    if n%2==0:
        return s+(n//2)*m-n//2+1
    return s+(n//2)*m-n//2+2
# 4043. Count Rotations With Exactly K Equal Adjacent Pairs
 




def countRotations(s,k):
    n=len(s)
    ans=0
    for _ in range(n):
        currscore=0
        for i in range(n-1):
            if s[i]==s[i+1]:
                currscore+=1
        if currscore==k:
            ans+=1
        s=s[1:n]+s[0]
    return ans
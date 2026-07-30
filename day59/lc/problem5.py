# 3014. Minimum Number of Pushes to Type Word I


def minimumPushes(word):
    n=len(word)
    ans=0
    t=1
    while n>=8:
        n-=8
        ans+=t*8
        t+=1
    ans+=t*n
    return ans
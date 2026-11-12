# 4090. Count Magical Substring Pairs I




def countMagicalPairs(s):
    n=len(s)
    ans=0
    for j in range(n-1):
        left=[0]*27
        right=[0]*27
        seen=set()
        for i in range(j,-1,-1):
            seen.add(s[i])
            left[len(seen)]+=1
        seen.clear()
        for k in range(j+1,n):
            seen.add(s[k])
            right[len(seen)]+=1
        for d in range(1,27):
            ans+=left[d]*right[d]
    return ans
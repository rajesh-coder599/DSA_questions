# 4007. Widest Possible Fence




def maximumWidth(planks):
    from collections import defaultdict
    freqofplanks=defaultdict(int)
    usedind=defaultdict(set)
    n=len(planks)
    for i in range(n):
        a=planks[i]
        freqofplanks[a]+=1
        for j in range(i+1,n):
            b=planks[j]
            if i in usedind and a+b in usedind[i]:
                continue
            if j in usedind and a+b in usedind[j]:
                continue
            usedind[j].add(a+b)
            usedind[i].add(a+b)
            freqofplanks[a+b]+=1
    ans=0
    for v in freqofplanks.values():
        ans=max(ans,v)
    return ans
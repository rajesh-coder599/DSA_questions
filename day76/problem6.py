# 1202. Smallest String With Swaps



def smallestStringWithSwaps(s,pairs):
    n=len(s)
    parent=list(range(n))
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    for i,j in pairs:
        parent[find(j)]=find(i)
    groups={}
    for i in range(n):
        root=find(i)
        if root not in groups:
            groups[root]=[]
        groups[root].append(i)
    result=list(s)
    for indicec in groups.values():
        charachters=[s[i] for i in indicec]
        charachters.sort()
        i=0
        l=len(charachters)
        while i<l:
            result[indicec[i]]=charachters[i]
            i+=1
    return "".join(result)
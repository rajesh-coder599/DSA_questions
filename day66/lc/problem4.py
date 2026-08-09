# 4015. Weighted Sum of a Tree





def weightedSum(parent,nums):
    from collections import defaultdict,deque
    child=defaultdict(list)
    n=len(parent)
    for i in range(1,n):
        child[parent[i]].append(i)
    h=0
    q=deque([0])
    while q:
        h+=1
        l=len(q)
        for _ in range(l):
            node=q.popleft()
            if node in child:
                for i in child[node]:
                    q.append(i)
    q=deque([(0,1)])
    ans=0
    while q:
        n,d=q.popleft()
        ans+=nums[n]*(h-d+1)
        if n in child:
            for node in child[n]:
                q.append((node,d+1))
    return ans
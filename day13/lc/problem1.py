# 1665. Minimum Initial Energy to Finish Tasks
import heapq


tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]


def minimumEffort(tasks):
    h=[]
    for i in tasks:
        a=(i[1]-i[0])
        heapq.heappush(h,[-a,i[0],i[1]])

    ans=0
    curr=0
    while h:
        x=heapq.heappop(h)
        mn=x[2]
        tc=x[1]
        if curr<mn:
            k=mn-curr
            curr+=k
            ans+=k
        curr-=tc
    return ans

print(minimumEffort(tasks))
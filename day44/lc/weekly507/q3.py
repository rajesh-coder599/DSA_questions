# Q3. Shortest Path With At Most K Consecutive Identical Characters


## got TLE in contest
from collections import defaultdict,deque
def shortestPath(n,edges,labels,k):
    adj=[]
    for _ in range(n):
        adj.append([])
    for x,y,z in edges:
        adj[x].append((y,z))
    q=deque([(0,labels[0],1)])
    cost=[float("inf")]*n
    cost[0]=0
    a=set()
    a.add((0,0))
    while q:
        node,currch,currfreq=q.popleft()
        for i,j in adj[node]:
            if labels[i] != currch and (i,cost[node]+j) not in a:
                cost[i]=min(cost[i],cost[node]+j)
                q.append((i,labels[i],1))
                a.add((i,cost[node]+j))
            else:
                if currfreq<k and (i,cost[node]+j) not in a:
                    cost[i]=min(cost[i],cost[node]+j)
                    q.append((i,currch,currfreq+1))
                    a.add((i,cost[node]+j))
    if cost[n-1]==float("inf") :
        return -1
    return cost[n-1]
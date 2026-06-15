# 3558. Number of Ways to Assign Edge Weights I


from collections import deque,defaultdict
def assignEdgeWeights(edges):
    graph=defaultdict(list)

    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
    q=deque([(1,0)])
    depth=0
    visited={1}
    while q:
        node,d=q.popleft()
        depth=max(depth,d)
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei,d+1))
    
    mod=10**9+7
    return pow(2,depth-1,mod)
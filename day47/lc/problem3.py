# 886. Possible Bipartition


from collections import deque
def possibleBipartition(n,dislikes):
    graph=[]
    for i in range(n):
        graph.append([])
    for x,y in dislikes:
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    colour=[-1]*n
    for i in range(n):
        if colour[i]!=-1:
            continue
        q=deque([i])
        colour[i]=0
        while q:
            node=q.popleft()
            for nei in graph[node]:
                if colour[nei]==-1:
                    colour[nei]=1-colour[node]
                    q.append(nei)
                elif colour[nei]==colour[node]:
                    return False
    return True
# 785. Is Graph Bipartite?


from collections import deque
def isBipartite(graph):
    n=len(graph)
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
                elif colour[node]==colour[nei]:
                    return False
    return True
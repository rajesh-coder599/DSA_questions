# 684. Redundant Connection



def findRedundantConnection(edges):
    n=len(edges)
    parent=list(n+1)
    def find(x):
        if parent[x] != x :
            parent[x]=find(parent[x])
        return parent[x]
    for u,v in edges:
        pu,pv=find(u),find(v)

        if pu==pv:
            return [u,v]
        parent[pu]=pv
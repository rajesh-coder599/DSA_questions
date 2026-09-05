# 685. Redundant Connection II



def findRedundantDirectedConnection(edges):
    n=len(edges)
    parent=[0]*(n+1)
    a=None
    b=None
    for u,v in edges:
        if  parent[v]==0:
            parent[v]=u
        else:
            a=[parent[v],v]
            b=[u,v]
            break
    dsu=list(range(n+1))
    def find(x):
        if dsu[x] != x:
            dsu[x]=find(dsu[x])
        return dsu[x]
    for u,v in edges:
        if [u,v]==b:
            continue
        pu=find(u)
        pv=find(v)
        if pu==pv:
            if a:
                return a
            else:
                return [u,v]
        dsu[pu]=pv
    return b
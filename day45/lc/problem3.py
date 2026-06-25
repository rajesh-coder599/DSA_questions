# 399. Evaluate Division


from collections import defaultdict,deque
def calcEquation(equations,values,queries):
    n=len(values)
    adj=defaultdict(list)
    for i in range(n):
        a,b=equations[i]
        v=values[i]
        adj[a].append((b,v))
        adj[b].append((a,1/v))
    arr=[]
    for x,y in queries:
        if x not in adj or y not in adj:
            arr.append(-1)
            continue
        ans=set()
        vis=set()
        q=deque([(x,1)])
        vis.add(x)
        while q:
            l=len(q)
            for _ in range(l):
                node,val=q.popleft()
                if node==y:
                    ans.add(val)
                    continue
                for a,b in adj[node]:
                    if a not in vis:
                        vis.add(a)
                        q.append((a,b*val))
        if len(ans) != 1 :
            arr.append(-1)
        else:
            arr.append(list(ans)[0])
    return arr

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
print(calcEquation(equations,values,queries))
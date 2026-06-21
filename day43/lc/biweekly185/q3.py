# Q3. Finish Time of Tasks I


from collections import defaultdict,deque
def finishTime(n,edges,baseTime):
    chilldren=defaultdict(list)
    for p,c in edges:
        chilldren[p].append(c)
    
    def dfs(i):
        if not chilldren[i]:
            return baseTime[i]
        
        vals=[dfs(v) for v in chilldren[i]]

        mn=min(vals)
        mx=max(vals)

        return mx+(mx-mn)+baseTime[i]
    return dfs(0)
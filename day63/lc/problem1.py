# 3310. Remove Methods From Project



def remainingMethods(n,k,invocations):
    from collections import deque
    adj=[]
    for _ in range(n):
        adj.append([])
    for a,b in invocations:
        adj[a].append(b)
    suspisiousmethods={k}
    q=deque([k])
    seen=set()
    while q:
        s_method=q.popleft()
        if s_method in seen:
            continue
        seen.add(s_method)
        for invoke_method in adj[s_method]:
            if invoke_method in seen:
                continue
            q.popleft(invoke_method)
            suspisiousmethods.add(invoke_method)
    for a,b in invocations:
        adj[b].append(a)
    groups={}
    vis=[False]*n
    currgroup=1
    for i in range(n):
        if vis[i]:
            continue
        q=deque([i])
        temp={i}
        while q:
            method=q.popleft()
            if vis[method]:
                continue
            vis[method]=True
            for x in adj[method]:
                if vis[x]:
                    continue
                temp.add(x)
                q.append(x)
        groups[currgroup]=temp
        currgroup+=1
    ans=[]
    for v in groups.values():
        if v==suspisiousmethods:
            continue
        for i in v:
            ans.append(i)
    return ans
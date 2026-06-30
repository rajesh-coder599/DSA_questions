# 947. Most Stones Removed with Same Row or Column


from collections import defaultdict,deque
def removeStones(stones):
    row=defaultdict(list)
    col=defaultdict(list)
    for r,c in stones:
        row[r].append((r,c))
        col[c].append((r,c))
    vis=set()
    ans=0
    for i,j in stones:
        temp=0
        if (i,j) in vis:
            continue
        q=deque([(i,j)])
        while q:
            r,c=q.popleft()
            for x in row[r]:
                if (x[0],x[1]) not in vis:
                    temp+=1
                    q.append((x[0],x[1]))
                    vis.add((x[0],x[1]))
            for y in col[c]:
                if (y[0],y[1]) not in vis:
                    temp+=1
                    q.append((y[0],y[1]))
                    vis.add((y[0],y[1]))
        ans+=temp
    return ans
# 3975. Filter Occupied Intervals

import heapq
def filterOccupiedIntervals(occupiedIntervals,freeStart,freeEnd):
    hq=[]
    for i in occupiedIntervals:
        heapq.heappush(hq,i)
    ans=[]
    while hq:
        a,b=heapq.heappop(hq)
        check=True
        if ans:
            x,y=ans[-1]
            if y+1>=a:
                check=False
                if b<=y:
                    continue
                elif b<freeStart or x>freeEnd:
                    ans[-1]=[x,b]
                elif b<=freeEnd:
                    ans[-1]=[x,freeStart-1]
                else:
                    ans[-1]=[x,freeStart-1]
                    ans.append([freeEnd+1,b])
        if check:
            if b<freeStart or a>freeEnd:
                ans.append([a,b])
            elif a<freeStart and b<=freeEnd:
                ans.append([a,freeStart-1])
            elif a<freeStart and b>freeEnd:
                ans.append([a,freeStart-1])
                ans.append([freeEnd+1,b])
            elif a>=freeStart and a<=freeEnd and b>freeEnd:
                ans.append([freeEnd+1,b])
    return ans
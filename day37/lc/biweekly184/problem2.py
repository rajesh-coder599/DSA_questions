# Q2. Minimum Energy to Maintain Brightness©leetcode

import heapq
def minEnergy(n,brightness,intervals):
    onbulb=brightness//3+(1 if brightness%3!=0 else 0)
    hq=[]
    for i in intervals:
        heapq.heappush(hq,i)
    totaltime=0
    a=heapq.heappop(hq)
    totaltime+=(a[1]-a[0]+1)
    endtime=a[1]
    while hq:
        st,en=heapq.heappop(hq)
        if st<=endtime and en<=endtime:
            continue
        if st<=endtime:
            totaltime+=(en-endtime)
            endtime=en
        else:
            totaltime+=(en-st+1)
            endtime=en
    return onbulb*totaltime
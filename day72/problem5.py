# 218. The Skyline Problem




def getSkyline(buildings):
    import heapq
    events=[]
    for l,r,h in buildings:
        events.append((l,-h))
        events.append((r,h))
    events.sort()
    hq=[0]
    skyline=[]
    prevmx=0
    live_heights={0:1}
    for x,h in events:
        if h<0:
            height=-h
            live_heights[height]=live_heights.get(height,0)+1
            heapq.heappush(hq,-height)
        else:
            height=h
            live_heights[height]-=1
        while hq and live_heights.get(-hq[0],0)==0:
            heapq.heappop(hq)
        currmx=-hq[0]
        if currmx!=prevmx:
            skyline.append([x,currmx])
            prevmx=currmx
    return skyline

# Q2. Minimum Lights to Illuminate a Road©leetcode


def minLights(lights):
    n=len(lights)
    vis=[0]*n
    for i in range(n):
        v=lights[i]
        if v>0:
            l=max(0, i - v)
            r=min(n - 1, i + v)
            vis[l]+=1
            if r+1<n:
                vis[r+1]-=1
    perfix=[]
    perfix.append(vis[0])
    for x in range(1,n):
        x=perfix[-1]+vis[x]
        perfix.append(x)
    ans=0
    currcount=0
    for x in perfix:
        if x==0:
            currcount+=1
        else:
            if currcount>0:
                currcount=0
                ans+=1
        if currcount==3:
            currcount=0
            ans+=1
    if currcount>0:
        ans+=1
    return ans
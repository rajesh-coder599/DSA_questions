# 4026. Maximum Gap Between Stations



def maximumGap(skill,station):
    n=len(station)
    m=len(skill)
    if m==1:
        return 0
    i=0
    early=[]
    late=[]
    for j in range(n):
        if station[j]==skill[i]:
            early.append(j)
            i+=1
            if i==m:
                break
    i=m-1
    for j in range(n-1,-1,-1):
        if station[j]==skill[i]:
            late.append(j)
            i-=1
            if i<0:
                break
    mxgap=1
    for i in range(1,m):
        mxgap=max(mxgap,abs(early[i-1]-late[i]))
    return mxgap
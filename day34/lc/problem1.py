# 3635. Earliest Finish Time for Land and Water Rides II


def earliestFinishTime(landStartTime,landDuration,waterStartTime,waterDuration):
    n=len(landStartTime)
    m=len(waterStartTime)
    lt=[]
    for i in range(n):
        lt.append(landStartTime[i]+landDuration[i])
    mn_ti=float("inf")
    a=min(lt)
    for i in range(m):
        if waterStartTime[i]<=a:
            mn_ti=min(mn_ti,a+waterDuration[i])
        else:
            mn_ti=min(mn_ti,waterStartTime[i]+waterDuration[i])
    wt=[]
    for j in range(m):
        wt.append(waterStartTime[j]+waterDuration[j])
    b=min(wt)
    for j in range(n):
        if landStartTime[j]<=b:
            mn_ti=min(mn_ti,b+landDuration[j])
        else:
            mn_ti=min(mn_ti,landStartTime[j]+landDuration[j])
    return mn_ti

ls=[2,8]
ld=[4,1]
ws=[6]
wd=[3]
print(earliestFinishTime(ls,ld,ws,wd))
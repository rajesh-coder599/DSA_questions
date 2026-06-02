# 3633. Earliest Finish Time for Land and Water Rides I


def earliestFinishTime(landStartTime,landDuration,waterStartTime,waterDuration):

    n=len(landStartTime)
    m=len(waterStartTime)
    mn_ti=float("inf")
    for i in range(n):
        a=landStartTime[i]+landDuration[i]
        for j in range(m):
            if waterStartTime[j]>=a:
                b=waterStartTime[j]+waterDuration[j]
                
            else:
                b=a+waterDuration[j]
            mn_ti=min(mn_ti,b)
    for i in range(m):
        a=waterStartTime[i]+waterDuration[i]
        for j in range(n):
            if landStartTime[j]>=a:
                b=landStartTime[j]+landDuration[j]
                
            else:
                b=a+landDuration[j]
            mn_ti=min(mn_ti,b)
            
    
    return mn_ti
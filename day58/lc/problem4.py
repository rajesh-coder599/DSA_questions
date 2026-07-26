# 4001. Aggregate Two Time Series




def aggregateTimeSeries(series1,series2):
    arr=[]
    n=len(series1)
    m=len(series2)
    i=0
    j=0
    while i<n and j<m:
        t1,v1=series1[i]
        t2,v2=series2[j]
        a=min(t1,t2)
        b=v1+v2
        temp=[a,b]
        if t1==t2:
            i+=1
            j+=1
        elif t1<t2:
            i+=1
        else:
            j+=1
        arr.append(temp)
    if i>=n and j>=m :
        return arr
    if i<n:
        while i<n:
            a,b=series1[i]
            arr.append([a,b])
            i+=1
    if j<m :
        while j<m :
            a,b=series2[j]
            arr.append([a,b])
            j+=1
    return arr
series1 = [[19,236]]
series2 = [[1,79],[30,726]]
print(aggregateTimeSeries(series1,series2))
# 1606. Find Servers That Handled Most Number of Requests


def busiestServers(k,arrival,load):
    n=len(arrival)
    free_time=[0]*k
    freq=[0]*k
    for i in range(n):
        for j in range(k):
            if free_time[(i+j)%k]<=arrival[i]:
                free_time[(i+j)%k]=arrival[i]+load[i]
                freq[(i+j)%k]+=1
                break
    x=max(freq)
    ans=[]
    for i in range(k):
        if freq[i]==x:
            ans.append(i)
    return ans
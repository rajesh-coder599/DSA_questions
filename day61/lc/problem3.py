# 4012. Count of Unfinished Tasks After Each Shift




def countTasks(tasks,shifts):
    perfixoftime=[tasks[0]]
    n=len(tasks)
    for i in range(1,n):
        temp=perfixoftime[-1]+tasks[i]
        perfixoftime.append(temp)
    def upperbound(target):
        l=0
        r=n-1
        ans=n
        while l<=r:
            mid=(l+r)//2
            if perfixoftime[mid]<=target:
                l=mid+1
            else:
                r=mid-1
                ans=mid
        return ans
    m=len(shifts)
    ans=[]
    prev=0
    for i in range(m):
        t=shifts[i]
        a=t+prev
        x=upperbound(a)
        ans.append(n-x)
        if n-x==0 or x==0:
            prev=0
        else:
            prev+=shifts[i]
    return ans
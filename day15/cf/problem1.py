# 218D. OutOfMemoryError


t=int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    arr=list(map(int,input().split()))

    extra=[0]*n
    last=[0]*n
    reset=0
    for _ in range(m):
        i,c=map(int,input().split())

        i-=1
        if last[i]!=reset:
            extra[i]=0
            last[i]=reset

        extra[i]+=c

        if extra[i]+arr[i]>h:
            reset+=1

    ans=[]

    for i in range(n):
        if last[i]!=reset:
            ans.append(arr[i])
        else:
            ans.append(arr[i]+extra[i])

    print(*ans)
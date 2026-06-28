# B. Array


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    for i in range(n-1):
        a=arr[i]
        g=0
        s=0
        for j in range(i+1,n):
            if arr[j]>a:
                g+=1
            elif arr[j]<a:
                s+=1
        ans.append(max(g,s))
    ans.append(0)
    print(*ans)
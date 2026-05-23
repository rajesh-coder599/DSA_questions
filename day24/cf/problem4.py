# 2229B. Absolute Cinema


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        if a[i]>b[i]:
            a[i],b[i]=b[i],a[i]

    x=max(a)
    y=sum(b)
    print(x+y)
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    x=list(map(int,input().split()))
    sum1=sum(a)
    for _ in range(m):
        p=min(a)
        a.remove(p)
        if p<0:
            continue
        sum1-=p
    print(sum1)
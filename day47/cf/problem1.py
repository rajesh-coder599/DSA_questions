# A. Another Popcount Problem


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k>=n:
        print(n)
        continue
    ans=0
    a=n//k
    x=1
    while x*2-1<=a:
        x=x*2
    temp=n-x*k
    c=temp//x
    i=bin(x*2-1)
    j=i.count("1")
    if temp<x:
        c=0
    ans+=j*c
    p=bin(x-1)
    q=p.count("1")
    ans+=q*(k-c)
    print(ans)
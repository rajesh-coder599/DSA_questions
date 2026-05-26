# Magic Set


t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    seq=list(map(int,input().split()))
    ans=0
    for i in seq:
        if i%m==0:
            temp=(n*(n-1))//2
            ans+=temp

    print(ans)
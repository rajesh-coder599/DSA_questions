# Magic Set


t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    seq=list(map(int,input().split()))
    div=0
    for i in seq:
        if i%m==0:
            div+=1
    ans=(div*(div+1))//2
    if div==n:
        ans+=1
    print(ans)
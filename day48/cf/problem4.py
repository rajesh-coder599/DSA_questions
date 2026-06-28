# B. Crimson Triples



t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    for b in range(1,n+1):
        k=n//b
        ans+=k*k
    print(ans)
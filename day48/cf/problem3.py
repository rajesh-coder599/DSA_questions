# A. Another Puzzle from Papyrus



t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans1=0
    for i in range(n):
        if a[i]<b[i]:
            ans1=float("inf")
            break
        ans1+=abs(a[i]-b[i])
    ans2=c
    a.sort()
    b.sort()
    for i in range(n):
        if a[i]<b[i]:
            ans2=float("inf")
            break
        ans2+=abs(a[i]-b[i])
    ans=min(ans1,ans2)
    print(-1 if ans==float("inf") else ans)
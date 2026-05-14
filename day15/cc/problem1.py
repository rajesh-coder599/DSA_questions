# Chef and Work


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    weight=list(map(int,input().split()))
    ans=0
    curr=0
    check=True
    for i in weight:
        if i>k:
            check=False
            break
        if curr+i<=k:
            curr+=i
        else:
            curr=i
            ans+=1
    if check==False:
        print(-1)
        continue
    if curr>0:
        ans+=1
    print(ans)
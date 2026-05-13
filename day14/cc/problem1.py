# Hostel Room

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    ans=x
    curr=x
    for i in arr:
        curr+=i
        ans=max(curr,ans)
    
    print(ans)
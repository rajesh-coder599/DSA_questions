# Equality

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    x=sum(arr)//(n-1)
    for i in arr:
        ans.append(x-i)
    print(*ans)
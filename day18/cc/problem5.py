# Remove Element


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    if n==1:
        print("YES")
        continue
    a=max(arr)
    b=min(arr)
    if a+b>k:
        print("NO")
    else:
        print("YES")
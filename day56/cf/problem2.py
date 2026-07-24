# https://codeforces.com/problemset/problem/2237/C
# C. Duck Surplus


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    x=arr[0]
    if n==1:
        print(x)
        continue
    for i in range(1,n):
        if x>arr[i]:
            x+=arr[i]
        else:
            x=arr[i]
    print(x)
# A. Another Popcount Problem

## incomeplete
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k>=n:
        print(n)
        continue
    ans=0
    a=n//k

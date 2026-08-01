# https://codeforces.com/contest/2248/problem/B
# B. Merge to Match



t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if n<2*m:
        print("NO")
        continue
    a.sort()
    b.sort()
    first=True
    last=True
    for i in range(m):
        if a[i]>b[i]:
            first=False
            break
        if a[-i-1]<b[-i-1]:
            last=False
            break
    if first and last :
        print("YES")
    else:
        print("NO")
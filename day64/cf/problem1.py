# https://codeforces.com/problemset/problem/2247/B
# B. Yet Another Constructive



t=int(input())
for _ in range(t):
    n,k,m=map(int,input().split())
    if k>n or k>m:
        print("NO")
        continue
    ans=[1]*n
    ans[0]+=(m-k)
    print("YES")
    print(*ans)
# https://codeforces.com/contest/2248/problem/C
# C. Maximize the Score



t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    from collections import defaultdict
    idxof=defaultdict(list)
    for i in range(2*n):
        idxof[arr[i]].append(i)
    dp=[0]*(2*n+1)
    for i in range(2*n):
        l,r=idxof[arr[i]]
        if i==l:
            dp[i+1]=dp[i]+1
        else:
            dp[i+1]=max(dp[i]+1,dp[l]+(r-l+1)**2)
    print(dp[2*n])
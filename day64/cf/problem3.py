# https://codeforces.com/contest/2252/problem/A
# A. Boss Fight



t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    ans=0
    for k,v in freq.items():
        if v-2>=(n-v):
            ans+=(n-v+2)*k
        else:
            ans+=v*k
    print(ans)
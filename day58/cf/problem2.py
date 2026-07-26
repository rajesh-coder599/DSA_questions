# https://codeforces.com/contest/2250/problem/B
# B. String Construction


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k+2>n:
        print(-1)
        continue
    x=k//2+k%2
    ans="1"*(k-x+1)
    ans+="0"*(x+1)
    # if k==1:
    #     ans="1"+ans
    # else:
    #     ans+="1"*(k-x+1)
    for _ in range(n-k-2):
        a=ans[-1]
        if a=="0":
            ans+="1"
        else:
            ans+="0"
    print(ans)
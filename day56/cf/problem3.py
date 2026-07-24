# https://codeforces.com/problemset/problem/2237/B
# B. Annoying the Ghost


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    opr=0
    ans=True
    for i in range(n):
        if a[i]>b[i]:
            found=False
            idx=None
            for j in range(i,n):
                if a[j]<=b[i]:
                    found=True
                    idx=j
                    break
            if not found :
                ans=False
                break
            for x in range(idx,i,-1):
                a[x],a[x-1]=a[x-1],a[x]
                opr+=1
    if ans :
        print(opr)
    else:
        print(-1)
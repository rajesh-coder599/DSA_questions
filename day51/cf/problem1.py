# C. Shifted MEX


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    mex=1
    currmex=1
    x=-a[0]
    for i in range(1,n):
        if a[i-1]==a[i]:
            continue
        if x+a[i]==currmex:
            currmex+=1
            mex=max(mex,currmex)
        else:
            x=-a[i]
            currmex=1
    print(mex)
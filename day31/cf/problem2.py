# 2232A. Convergence


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    if n%2==1:
        ind=n//2
        a=arr[ind]
        x=arr[:ind].count(a)
        y=arr[ind+1:].count(a)
        ans=ind-min(x,y)
        print(ans)
    else:
        ind1=n//2
        ind2=ind1-1
        a=arr[ind1]
        if arr[ind1]!=arr[ind2]:
            print(ind1)
            continue
        x=arr[:ind1].count(a)
        y=arr[ind1:].count(a)
        ans=(n//2)-min(x,y)
        print(ans)
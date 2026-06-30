# D. An Alternative Way


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if a[0]>b[0]:
        print("NO")
        continue
    currdiff=abs(a[0]-b[0])
    check=True
    l=0
    for i in range(1,n):
        if (i-l)%2==0:
            if a[i]>b[i]:
                check=False
                break
            else:
                currdiff=abs(a[i]-b[i])
                l=i
        else:
            if a[i]<=b[i]:
                currdiff=abs(a[i]-b[i])
                l=i
            else:
                k=a[i]-b[i]
                if k!=currdiff:
                    check=False
                    break
    if check:
        print("YES")
    else:
        print("NO")
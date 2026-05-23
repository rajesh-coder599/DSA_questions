# 2229C1. We Be Flipping (Easy Version)


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if max(a)<0:
        print(0)
        continue
    k=0
    arr=[]
    curr=1
    if a[0]<0:
        curr=-1
    for i in range(1,n):
        if (a[i]>0 and a[i-1]<0) or (a[i]<0 and a[i-1]>0):
            k+=1
            arr.append(i)
    if a[-1]>0:
        arr.append(n)
        k+=1
    arr.reverse()
    print(k)
    print(*arr)
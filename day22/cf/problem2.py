# 2231B. Another Sorting Problem


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1 or n==2:
        print("YES")
        continue

    first=arr[0]
    currmx=None
    currmn=None
    for i in range(1,n):
        if arr[i]<first:
            currmn=arr[i]
            currmx=first
            break
        elif arr[i]>first:
            currmx=arr[i]
            currmn=first
            break
    if currmx==currmn:
        print("YES")
        continue
    check=True
    for i in range(1,n):
        a=arr[i]
        if a<first:
            if a<currmn:
                check=False
                break
            currmn=a
        else:
            if a<currmx:
                check=False
                break
            currmx=a
    
    if check:
        print("YES")
    else:
        print("NO")

## WA
# 2231B. Another Sorting Problem


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1 or n==2:
        print("YES")
        continue
    k=0
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            temp=arr[i-1]-arr[i]
            k=max(k,temp) 
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            arr[i]+=k
            
    check=True
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            check=False
            break

    if check:
        print("YES")
    else:
        print("NO")
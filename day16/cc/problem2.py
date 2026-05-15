# Ups and Downs

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1:
        print(arr)
        continue
    arr.sort()
    if n%2==0:
        n-=1
    for i in range(1,n,2):
        x=min(arr[i],arr[i+1])
        y=max(arr[i],arr[i+1])
        arr[i]=y
        arr[i+1]=x

    print(arr)


# Average Permutation


t=int(input())
for _ in range(t):
    n=int(input())
    if n==3:
        print(1,2,3)
        continue

    arr=[0]*n
    arr[0]=n
    arr[n-1]=n-1
    arr[1]=n-2
    arr[n-2]=n-3
    for i in range(2,n-2):
        arr[i]=i-1

    print(*arr)
# Alternating Divisibility


t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
        continue
    arr=[-1]*n
    for i in range(1,n+1,2):
        arr[i-1]=i
    for j in range(1,n,2):
        a=2*arr[j-1]
        arr[j]=a
    # if arr[-1]==-1:
    #     arr[-1]=arr[-2]*2
    print(*arr)

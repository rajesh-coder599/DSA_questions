# Array Halves

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a=2*n-1
    ans=0
    for i in range(2*n-1,-1,-1):
        if arr[i]>n:
            temp=a-i
            ans+=temp
            a-=1
    print(ans)
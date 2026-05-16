# 2094C. Brr Brrr Patapim

t=int(input())
for _ in range(t):
    n=int(input())
    mat=[list(map(int,input().split())) for _ in range(n)]
    ans_arr=[-1]*(2*n)
    for i in range(n):
        val=mat[i][0]
        ans_arr[i+1]=val
    for j in range(1,n):
        val=mat[n-1][j]
        ans_arr[n+j]=val
    a=set(ans_arr)
    for num in range(1,2*n+1):
        if num not in a:
            ans_arr[0]=num
        
    print(*ans_arr)
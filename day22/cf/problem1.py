# 2231A. Construct an Array

t=int(input())
for _ in range(t):
    n=int(input())
    ans=[]
    for i in range(n+1,2*n+1):
        ans.append(i)

    print(*ans)
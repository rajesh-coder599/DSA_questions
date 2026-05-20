# 2147B. Multiple Construction


t=int(input())
for _ in range(t):
    n=int(input())
    ans=[]
    for i in range(n-1,0,-1):
        ans.append(i)
    
    ans.append(n)
    for i in range(1,n+1):
        ans.append(i)

    print(*ans)
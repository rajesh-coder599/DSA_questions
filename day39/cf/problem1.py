# B. Different Distances


t=int(input())
for _ in range(t):
    n=int(input())
    if n==2:
        print(*[2,1,1,2,1,2,2,1])
        continue
    a=[]
    b=[]
    for i in range(1,n+1):
        a.append(i)
        a.append(i)
        b.append(i)
    for i in range(1,n+1):
        b.append(i)
    ans=a+b
    ans[0],ans[-1]=ans[-1],ans[0]
    print(*ans)
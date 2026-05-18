# Average Array

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    ans=[]
    if n%2!=0:
        a=n//2
        for i in range(a+1):
            ans.append(x-i)

        for i in range(1,a+1):
            ans.append(x+i)

    else:
        a=n//2
        for i in range(1,a+1):
            ans.append(x-i)

        for i in range(1,a+1):
            ans.append(x+i)
    
    print(*ans)
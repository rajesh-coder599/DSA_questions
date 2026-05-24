# Control the Pollution


t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    if x<=y*25:
        b=n//100
        rem=n%100
        ans=b*x
        ans+=min(x,((rem+3)//4)*y)
    else:
        ans=((n+3)//4)*y
    print(ans)
# Jogging


t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    ans=x*pow(2,n-1,1000000007)
    print(ans)
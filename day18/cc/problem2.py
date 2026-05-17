# Bella ciao


t=int(input())
for _ in range(t):
    D,d,p,q=map(int,input().split())
    ans=D*p
    D-=d
    a=D//d
    b=d*q*((a*(a+1))//2)
    ans+=b
    c=D%d
    ans+=(c*(a+1)*q)
    print(ans)
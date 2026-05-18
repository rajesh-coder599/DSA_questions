# 2230A. Optimal Purchase


t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    if 3*a<=b:
        print(n*a)
    else:
        temp=n//3
        rem=n%3
        ans=temp*b
        if rem*a<b:
            ans+=rem*a
        else:
            ans+=b
        print(ans)
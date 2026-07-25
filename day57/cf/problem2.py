# https://codeforces.com/problemset/problem/2226/B
# B. Everything Everywhere


def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    ans=0
    for i in range(n-1):
        x=p[i]
        y=p[i+1]
        if gcd(x,y)==abs(x-y):
            ans+=1
    print(ans)
# https://codeforces.com/contest/2254/problem/A
# A. Riptide



t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x=max(a,b,c)
    y=min(a,b,c)
    z=a+b+c-x-y
    if (x-y)%2 != 0:
        print(min((x-z),(z-y)))
    else:
        print(min((x-y)//2,(z-y),(x-z)))
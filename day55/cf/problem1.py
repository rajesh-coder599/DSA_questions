# https://codeforces.com/problemset/problem/2241/D
# D. An Alternative Way



t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    t=0
    check=True
    for i in range(n):
        temp=abs(a[i]-b[i])
        if a[i]>b[i]:
            if t<temp:
                check=False
                break
            else:
                t=min(t,temp)
        elif a[i]<b[i]:
            t=temp+t
    if check:
        print("YES")
    else:
        print("NO")
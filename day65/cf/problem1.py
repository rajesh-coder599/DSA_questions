# https://codeforces.com/contest/2253/problem/A
# A. The Best Card



t=int(input())
for _ in range(t):
    n=int(input())
    ans=True
    for i in range(2,n):
        if (n+1)%i == 0:
            ans=False
            break
    if ans:
        print("YES")
    else:
        print("NO")
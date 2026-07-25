# https://codeforces.com/problemset/problem/2218/D
# D. The 67th OEIS Problem


t=int(input())
for _ in range(t):
    n=int(input())
    arr=[1]
    for i in range(3,n*2+1,+2):
        arr.append((i-2)*i)
    print(*arr)
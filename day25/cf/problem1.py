# 1328A. Divisibility Problem


t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a%b==0:
        print(0)
        continue
    print(b-a%b)
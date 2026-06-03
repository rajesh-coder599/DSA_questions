# B. Remilia Plays Soku


t=int(input())
for _ in range(t):
    n,x1,x2,k=map(int,input().split())
    if n<4:
        print(1)
        continue
    ans=min(abs(x1-x2),n-abs(x1-x2))
    print(ans)
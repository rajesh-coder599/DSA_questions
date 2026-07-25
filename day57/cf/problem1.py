# https://codeforces.com/problemset/problem/2228/B
# B. Remilia Plays Soku


t=int(input())
for _ in range(t):
    n,x1,x2,k=map(int,input().split())
    if n<=3:
        print(1)
        continue
    moves=k
    d1=abs(x1-x2)
    d2=n-d1
    if d1==d2:
        moves+=d1
    elif abs(d1-d2)==1:
        moves+=min(d1,d2)
    else:
        moves+=min(d1,d2)
    print(moves)
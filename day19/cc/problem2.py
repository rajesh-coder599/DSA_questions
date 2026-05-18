# Decreasing Srrnmieeda

t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    if l+l-1<r:
        print(-1)
        continue

    print(r)
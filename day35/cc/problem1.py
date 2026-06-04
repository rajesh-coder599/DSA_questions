# Chef Odd


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n//k<2:
        print("NO")
        continue
    e=n//2
    o=n-e
    if o<k:
        print("NO")
    elif o==k:
        print("YES")
    else:
        x=o-k
        if x%2==0:
            print("YES")
        else:
            print("NO")
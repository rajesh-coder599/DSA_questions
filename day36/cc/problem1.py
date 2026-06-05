# Three Friends


t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if abs(x-z)==y or abs(z+x)==y or abs(z-x)==y :
        print("YES")
    else:
        print("NO")
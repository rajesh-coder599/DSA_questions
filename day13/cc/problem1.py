# Elections in Chefland

t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x=max(a,b,c)
    if x<=50:
        print("NOTA")
    else:
        if a>b and a>c:
            print("A")
        elif b>c:
            print("B")
        else:
            print("C")
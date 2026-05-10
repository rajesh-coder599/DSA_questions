# new year cake

t=int(input())
for _ in range(t):
    d,w=map(int,input().split())
    d1=d
    w1=w
    d2=d
    w2=w
    l1=0
    l2=0
    c1=1
    c2=1
    # white
    while True:
        if l1%2==0:
            if c1<=w1:
                w1-=c1
                l1+=1
            else:
                break
        else:
            if c1<=d1:
                d1-=c1
                l1+=1
            else:
                break
        c1*=2

    # dark
    while True:
        if l2%2==0:
            if c2<=d2:
                d2-=c2
                l2+=1
            else:
                break
        else:
            if c2<=w2:
                w2-=c2
                l2+=1
            else:
                break
        c2*=2

    print(max(l1,l2))
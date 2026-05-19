# Full Barrier Alchemist


t=int(input())
for _ in range(t):
    n,h,y1,y2,l=map(int,input().split())
    passed=0
    for _ in range(n):

        t,x=map(int,input().split())
        if l==0:
            continue
        if t==1:
            if x>=h-y1:
                passed+=1
            else:
                passed+=1
                l-=1
        else:
            if x<=y2:
                passed+=1
            else:
                passed+=1
                l-=1

    if l==0:
        passed-=1
    print(passed)

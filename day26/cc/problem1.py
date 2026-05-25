# Chef and Adventures


t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    
    p1=((n-1)%x==0 and (m-1)%y==0)

    p2=((n>=2 and m>=2) and ((n-2)%x==0 and (m-2)%y==0))

    if p1 or p2 :
        print("Chefirnemo")
    else:
        print("Pofik")
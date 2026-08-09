# https://codeforces.com/contest/2253/problem/C
# C. Sum of Distinct Values in a Matrix


## WA (i dont understand what to do!!)
t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.reverse()
    b.reverse()
    ans=0
    lasta=0
    lastb=0
    vis=set()
    r=0
    c=0
    extraina=[]
    for i in a:
        r+=1
        if r>n:
            extraina.append(i)
        else:
            vis.add(i)
            ans+=i
            lasta=i
    extrainb=[]
    k=0
    for j in b:
        if j in vis:
            k+=1
            continue
        c+=1
        if c>m:
            extrainb.append(j)
        else:
            vis.add(j)
            ans+=j
            lastb=j
    if k>0 :
        for i in extraina:
            if i in vis:
                continue
            k-=1
            if k<0:
                break
            else:
                ans+=i
                lasta=i
    ans-=min(lasta,lastb)

    print(ans)
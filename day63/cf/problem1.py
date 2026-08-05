# https://codeforces.com/contest/2254/problem/C1
# C1. Marenol (easy version)



t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    b=input()
    e1=[0,0]
    e2=[0,0]
    o1=[0,0]
    o2=[0,0]
    for i in range(n):
        if i%2==0:
            if a[i]=="0":
                e1[0]+=1
            else:
                e1[1]+=1
            if b[i]=="0":
                e2[0]+=1
            else:
                e2[1]+=1
        else:
            if a[i]=="0":
                o1[0]+=1
            else:
                o1[1]+=1
            if b[i]=="0":
                o2[0]+=1
            else:
                o2[1]+=1
    if e1==e2 and o1==o2 :
        print("YES")
    else:
        print("NO")
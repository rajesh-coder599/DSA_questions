# https://codeforces.com/contest/2254/problem/C1
# C1. Marenol (easy version)



t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    b=input()
    if a.count("1") != b.count("1") :
        print("NO")
        continue
    posaof1=[]
    posbof1=[]
    for i in range(n):
        if a[i]=="1":
            posaof1.append(i)
        if b[i]=="1" :
            posbof1.append(i)
    mismatch=0
    for i in range(len(posbof1)):
        x=posbof1[i]
        y=posaof1[i]
        if (x%2==0 and y%2!=0) or (x%2!=0 and y%2==0):
            mismatch+=1
    if mismatch==0:
        print("YES")
    else:
        print("NO")
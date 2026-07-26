# https://codeforces.com/contest/2250/problem/A
# A. Threshold Movement


t=int(input())
for _ in range(t):
    n=int(input())
    w=list(map(int,input().split()))
    if n%2!=0:
        print("NO")
        continue
    o=[]
    e=[]
    for i in range(n):
        if i%2==0:
            e.append(w[i])
        else:
            o.append(w[i])
    mx=max(o)
    mn=min(e)
    if (mn-mx)>=2 :
        print("YES")
    else:
        print("NO")
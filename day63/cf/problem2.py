# https://codeforces.com/problemset/problem/2247/C
# C. Inversion of a Subsequence



t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    one=0
    zero=0
    for i in range(n):
        if a[i]!=b[i]:
            if a[i]==1:
                one+=1
            else:
                zero+=1
    matchesone=sum(a)-one
    matcheszero=n-zero-one-matchesone
    if one==0 :
        if zero==0:
            print(0)
        elif matchesone>0 and matcheszero>0 :
            print(2)
        else:
            print(-1)
    elif one%2==0:
        print(2)
    else:
        print(1)
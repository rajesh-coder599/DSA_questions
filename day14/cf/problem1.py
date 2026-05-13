#  2184B. Hourglass

t=int(input())
for _ in range(t):
    s,k,m=map(int,input().split())
    if s<=k:
        a=m%k
        if a>=s:
            print(0)
        else:
            print(s-a)
    else:
        a=m//k
        b=m%k
        if a%2==0:
            print(0 if s<=b else s-b)
        else:
            print(0 if k<=b else k-b)
        
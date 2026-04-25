# ATM Machine
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    s=""
    for i in arr:
        if i<=k:
            k-=i
            s=s+"1"
        else:
            s=s+"0"
    print(s)

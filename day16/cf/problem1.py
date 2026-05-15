# 2169A. Alice and Bob

t=int(input())
for _ in range(t):
    n,a=map(int,input().split())
    arr=list(map(int,input().split()))
    h=0
    l=0
    for i in arr:
        temp = i-a
        if temp>0:
            h+=1
        elif temp<0:
            l+=1

    if l>h:
        print(a-1)
    else:
        print(a+1)
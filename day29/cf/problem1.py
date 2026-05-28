# 2191B. MEX Reordering


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if 0 not in arr:
        print("NO")
    elif 1 in arr:
        print("YES")
    else:
        a=arr.count(0)
        if a==1:
            print("YES")
        else:
            print("NO")
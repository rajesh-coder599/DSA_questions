# Fit to Play


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    mx_diff=0
    curr_min=float("inf")
    for i in arr:
        curr_min=min(curr_min,i)
        if i>curr_min:
            mx_diff=max(mx_diff,i-curr_min)
    if mx_diff==0:
        print("UNFIT")
    else:
        print(mx_diff)
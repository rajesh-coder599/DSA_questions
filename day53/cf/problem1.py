# https://codeforces.com/problemset/problem/2242/B
# B. Predominant Frequency Division


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    lesser=0
    greater=0
    first=False
    second=False
    for x in range(n):
        i=arr[x]
        if not first:
            if i>1:
                greater+=1
            else:
                lesser+=1
            if lesser>=greater:
                first=True
                lesser=0
                greater=0
        else:
            if i>2:
                greater+=1
            else:
                lesser+=1
            if lesser>=greater and x<n-1:
                second=True
    if first and second :
        print("YES")
    else:
        print("NO")
# 2210B. Simply Sitting on Chairs

t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if i>=(p[i]-1) :
            ans+=1
    print(ans)
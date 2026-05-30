# Digital clock

t=int(input())
for _ in range(t):
    h,m=map(int,input().split())
    ans=0
    for i in range(h):
        for j in range(m):
            s=str(i)+str(j)
            if len(set(s))==1:
                ans+=1
    print(ans)
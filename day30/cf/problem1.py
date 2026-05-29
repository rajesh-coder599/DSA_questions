# 268A. Games


n=int(input())
h=[]
g=[]
ans=0
for _ in range(n):
    hi,gi=map(int,input().split())
    a=h.count(gi)
    b=g.count(hi)
    h.append(hi)
    g.append(gi)
    ans+=(a+b)
print(ans)
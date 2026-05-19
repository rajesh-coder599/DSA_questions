# Permutation Xority


t=int(input())
for _ in range(t):
    n=int(input())
    if n==2:
        print(-1)
        continue
    ans=[]
    if n%2!=0:
        for i in range(1,n+1):
            ans.append(i)
    else:
        ans=[2,3,1,4]
        if n>4:
            for i in range(5,n+1):
                ans.append(i)
    print(*ans)
# 2227C. Snowfall

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    for i in arr:
        if i%6==0:
            ans.append(i)
    for i in arr:
        if i%6 != 0:
            if i%2==0:
                ans.append(i)

    for i in arr:
        if i%6 != 0 and i%2 != 0 and i%3 !=0 :
            ans.append(i)
    
    for i in arr:
        if i%6 != 0 and i%2 != 0 :
            if i%3==0:
                ans.append(i)

    print(*ans)
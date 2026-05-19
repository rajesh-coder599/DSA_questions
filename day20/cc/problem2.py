# Balanced and Unique Arrays


t=int(input())
for _ in range(t):
    n=int(input())
    temp=n//2
    if temp%2==1:
        print("NO")
        continue

    a=[]
    b=[]
    for i in range(1,n+1):
        if i<=temp//2 :
            a.append(i)
        elif i<=n-temp//2 :
            b.append(i)
        else:
            a.append(i)
        
    print("YES")
    print(*a)
    print(*b)
# Mighty Friend

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    m=[]
    t=[]
    for i in range(n):
        if i%2==0:
            m.append(arr[i])
        else:
            t.append(arr[i])
    
    m.sort(reverse=True)
    t.sort()
    for i in range(min(k,len(m),len(t))):
        if m[i]>t[i]:
            m[i],t[i]=t[i],m[i]
        else:
            break

    if sum(m)>=sum(t):
        print("NO")
    else:
        print("YES")
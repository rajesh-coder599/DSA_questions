# B. Annoying the Ghost


## wrong answer
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    inv=0
    for i in range(n):
        x=b[i]
        for j in range(i+1,n):
            if x>a[j]:
                inv+=1
    a.sort()
    check=True
    for x in range(n):
        if a[x]>b[x]:
            check=False
    if check:
        print(inv)
    else:
        print(-1)
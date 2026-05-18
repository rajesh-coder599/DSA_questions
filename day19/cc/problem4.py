# Parallel Processing

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    perfix=[0]*n
    perfix[0]=arr[0]
    for i in range(1,n):
        perfix[i]=perfix[i-1]+arr[i]

    t=[0]*n
    a=perfix[-1]
    for i in range(n):
        t[i]=max(perfix[i],a-perfix[i])
    
    final_ans=min(t)
    print(final_ans)
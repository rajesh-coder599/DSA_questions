# Hotel Bytelandia

t=int(input())
for _ in range(t):
    n=int(input())
    arrival=list(map(int,input().split()))
    departure=list(map(int,input().split()))
    m=max(departure)
    ans_arr=[0]*m
    for i in range(n):
        a=arrival[i]
        b=departure[i]
        for j in range(a,b):
            ans_arr[j-1]+=1

    print(max(ans_arr))
# Akash and Dinner


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    catagory=list(map(int,input().split()))
    time=list(map(int,input().split()))
    mn={}
    for i in range(n):
        if catagory[i] not in mn :
            mn[catagory[i]]=time[i]
        else:
            mn[catagory[i]]=min(time[i],mn[catagory[i]])

    if len(mn)<k:
        print(-1)
        continue

    arr=sorted(mn.values())
    print(sum(arr[:k]))
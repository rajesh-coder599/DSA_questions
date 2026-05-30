# 2232B. Cake Leveling


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    prefixsum=[arr[0]]
    for i in range(1,n):
        prefixsum.append(arr[i]+prefixsum[i-1])
    mn=arr[0]
    ans=[]
    for i in range(n):
        mn=min(mn,prefixsum[i]//(i+1))
        ans.append(mn)
    print(*ans)
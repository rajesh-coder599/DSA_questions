# Approximately II


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    currmn=float("inf")
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            a=abs(arr[i]+arr[j]-k)
            if currmn>a:
                currmn=a
                count=1
            elif currmn==a:
                count+=1
    
    print(currmn,count)
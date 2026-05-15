# Trace of Matrix


t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    for _ in range(n):
        temp=list(map(int,input().split()))
        arr.append(temp)
    
    mx_sum=0


    for row in range(n):
        i=row
        j=0
        curr_sum=0
        while i<n and j<n:
            curr_sum+=arr[i][j]
            i+=1
            j+=1
        mx_sum=max(mx_sum,curr_sum)
    
    for col in range(n):
        i=0
        j=col
        curr_sum=0
        while i<n and j<n:
            curr_sum+=arr[i][j]
            i+=1
            j+=1
        mx_sum=max(curr_sum,mx_sum)
    print(mx_sum)
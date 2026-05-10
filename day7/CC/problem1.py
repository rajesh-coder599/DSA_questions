# Chef Diet

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    rem_pro=0
    enough=True
    for i in range(n):
        if arr[i]+rem_pro<k:
            enough=False
            print("NO",i+1)
            break
        else:
            rem_pro+=arr[i]-k

    if enough:
        print("YES")
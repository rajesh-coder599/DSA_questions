# Cutting Pizza


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    peices=[]
    for i in range(1,n):
        peices.append(arr[i]-arr[i-1])

    x=sum(peices)
    peices.append(360-x)
    mn=min(peices)
    hcf=1
    for i in range(1,mn+1):
        check=True
        for j in peices:
            if j%i != 0 :
                check=False
                break
        if check:
            hcf=i

    ans=0
    for i in peices:
        ans+=(i//hcf-1)
    print(ans)
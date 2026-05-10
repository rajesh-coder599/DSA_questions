# adjacent sum parity

arr=list(map(int,input().split()))
curr="e"
n=len(arr)
for i in range(1,n):
    if arr[i-1] ==1:
        if curr=="e" :
            curr="o"
        else:
            curr="e"

if curr=="e" and arr[-1]==0:
    print(True)
elif curr=="o" and arr[-1]==1:
    print(True)
else:
    print(False)
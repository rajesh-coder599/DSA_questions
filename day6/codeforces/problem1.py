# 266B. queue at the scholl

n,t=map(int,input().split())
s=input()
arr=[]
for x in range(n):
    arr.append(s[x])
for i in range(t):
    check=False
    for j in range(n-1):
        if check==True:
            check=False
            continue
        if arr[j]=="B" and arr[j+1]=="G":
            arr[j],arr[j+1]=arr[j+1],arr[j]
            check=True

ans="".join(arr)
print(ans)
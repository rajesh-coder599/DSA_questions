# https://codeforces.com/contest/2253/problem/B
# B. Hypercarp and the Control Panel



t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n==1:
        print(1)
        continue
    new_arr=[arr[0],arr[1]]
    for i in range(2,n):
        if arr[i]!=new_arr[-1] or arr[i]!=new_arr[-2]:
            new_arr.append(arr[i])
    m=len(new_arr)
    doublesave=False
    singlesave=False
    equaladj=0
    for i in range(1,m):
        if new_arr[i-1]==new_arr[i]:
            if i+2<m and new_arr[i+1]==new_arr[i+2]:
                doublesave=True
            if i==m-2 or i-2==0 or (i+2<m and new_arr[i]!=new_arr[i+2]) or (i-2>0 and new_arr[i]!=new_arr[i-3]):
                singlesave=True
            equaladj+=1
    if doublesave:
        equaladj-=2
    elif singlesave :
        equaladj-=1
    print(m-equaladj)
# 2227D. Palindromex

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    first_zero=None
    second_zero=None
    for i in range(2*n):
        if arr[i]==0 :
            if first_zero==None:
                first_zero=i
            else:
                second_zero=i
    
    ans=1
    l1=first_zero
    r1=first_zero
    while l1>0 and r1<2*n-1 :
        if arr[l1-1] == arr[r1+1]:
            l1-=1
            r1+=1
        else:
            break

    for i in range(1,r1-l1+1+1):
        if i not in arr[l1:r1+1] :
            ans=max(ans,i)
            break

    l2=second_zero
    r2=second_zero
    while l2>0 and r2<2*n-1 :
        if arr[l2-1] == arr[r2+1]:
            l2-=1
            r2+=1
        else:
            break

    for i in range(1,r2-l2+1+1):
        if i not in arr[l2:r2+1] :
            ans=max(ans,i)
            break

    l3=first_zero
    r3=second_zero
    while l3<r3 :
        if arr[l3+1] == arr[r3-1]:
            l3+=1
            r3-=1
        else:
            break
    if l3>=r3:
        l3=first_zero
        r3=second_zero
        while l3>0 and r3<2*n-1 :
            if arr[l3-1] == arr[r3+1]:
                l3-=1
                r3+=1
            else:
                break
    

        for i in range(1,r3-l3+1+1):
            if i not in arr[l3:r3+1] :
                ans=max(ans,i)
                break
    print(ans)
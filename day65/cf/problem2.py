# https://codeforces.com/contest/2253/problem/B
# B. Hypercarp and the Control Panel



t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=1
    swap=False
    chance=False
    i=1
    while i<n:
        if arr[i]!=arr[i-1]:
            ans+=1
            i+=1
        else:
            if i+2<n and not swap and arr[i]!=arr[i+1] and arr[i+1]==arr[i+2]:
                swap=True
                i+=3
            elif i+1<n and arr[i]!=arr[i+1] :
                if i+2<n:
                    if arr[i]!=arr[i+2]:
                        chance=True
                else:
                    chance=True
                i+=1
            elif i-2>=0 and arr[i-2]!=arr[i-1]:
                if i-3>=0:
                    if arr[i-3]!=arr[i-1]:
                        chance=True
                else:
                    chance=True
                i+=1
            else:
                i+=1
    if swap:
        print(ans+3)
    elif chance:
        print(ans+1)
    else:
        print(ans)
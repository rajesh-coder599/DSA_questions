# B. Zhily and Mex and Max


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    a=max(arr)
    ans+=(a*n)
    arr.sort()
    freq=[0]*n
    for i in arr:
        if i<n:
            freq[i]+=1
    if a<n:
        freq[a]-=1
    if freq[0]==0:
        print(ans)
        continue
    x=[]
    for i in range(n):
        if freq[i]!=0:
            temp=(i+1)*freq[i]
            ans+=temp
            x.append(temp)
        else:
            ans+=(n-1-i)*(freq[i-1]+1)
            break
    print(x)
    print(freq)
    print(sum(x))
    print(ans)
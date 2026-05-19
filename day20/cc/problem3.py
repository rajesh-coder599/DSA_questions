# Maximum Angriness


t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if k>=n//2:
        print((n*(n-1))//2)
        continue

    ans=(n*(n-1))//2
    a=n-k
    b=(a*(a-1))//2
    ans-=b
    c=(k*(k-1))//2
    ans+=c
    x=n-2*k
    ans+=x*k
    print(ans)


### here is simpler way


# t=int(input())
# for _ in range(t):
#     n,k=map(int,input().split())
#     if k>=n//2:
#         print((n*(n-1))//2)
#         continue

#     ans=k*(2*n-2*k-1/2)
#     print(int(ans))
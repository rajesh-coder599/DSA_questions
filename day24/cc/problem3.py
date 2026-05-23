# Counting Flags


t=int(input())
for _ in range(t):
    n=int(input())
    ans=n*(n-1)*(2*(n**2)-5*n+4)
    print(ans)
# Majin Vegeta

def countprime(x):
    prime=[True]*(x+1)
    for i in range(2,x//2+1):
        if prime[i]==True:
            for j in range(i,x+1,i):
                prime[j]=False
    return prime
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=set(countprime(m))
    ans=0
    for i in range(n,m):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                ans+=1
    print(ans)

## wrong code
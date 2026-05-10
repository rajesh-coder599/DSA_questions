# weekly contest 500 Q2

# sum of prime between number and its reverse

#use sivie algorithm

n=13
r=int(str(n)[::-1])
ans=0
for i in range(min(n,r),max(n,r)+1):
    prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            prime=False
            break

    if prime:
        ans+=i

print(ans)
# 977A. Wrong Subtraction

n,k=map(int,input().split())
for _ in range(k):
    temp=n%10
    if temp==0:
        n//=10
    else:
        n-=1

print(n)

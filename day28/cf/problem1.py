# 705A. Hulk


n=int(input())
ans="I hate "
for i in range(n-1):
    if i%2==0:
        ans+="that I love "
    else:
        ans+="that I hate "
ans+="it"
print(ans)
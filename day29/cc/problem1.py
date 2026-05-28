# Chef and Numbers

def sm(n):
    a=str(n)
    ans=0
    for i in a:
        ans+=int(i)
    return ans
x=int(input())
start=x-len(str(x))*9-9
end=x
ans=0
for i in range(max(1,start),end):
    a=sm(i)
    b=sm(a)
    if i+a+b==x:
        ans+=1
print(ans)
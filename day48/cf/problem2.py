# C. Omsk Programmers


t=int(input())
for _ in range(t):
    a,b,x=map(int,input().split())
    if a<x and b<x:
        ans=min(abs(a-b),2)
        print(ans)
        continue
    ans=abs(a-b)
    mx=max(a,b)
    mn=min(a,b)
    operations=0
    while mx>mn or mn>mx:
        if mx>mn:
            mx//=x
            operations+=1
            ans=min(ans,operations+abs(mx-mn))
        elif mn>mx:
            mn//=x
            operations+=1
            ans=min(ans,operations+abs(mx-mn))
        else:
            ans=min(operations,ans)
            break
    print(ans)
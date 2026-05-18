# 2230C. Arrange the Numbers in a Circle


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    equal1=0
    greater1=0
    ans=0
    for i in arr:
        if i>1:
            ans+=i
            greater1+=1
        else:
            equal1+=1

    
    for i in arr:
        if equal1==0:
            break
        if i>1:
            if greater1==1:
                a=i//2
                if equal1>a:
                    ans+=a
                    equal1-=a
                else:
                    ans+=equal1
                    equal1=0
            else:
                temp=i-2
                a=temp//2
                if equal1>a:
                    ans+=a
                    equal1-=a
                else:
                    ans+=equal1
                    equal1=0

    print(ans if ans>=3 else 0)
# 2204C. Spring

t=int(input())
for i in range(t):
    a,b,c,m=map(int,input().split())
    al=0
    bo=0
    ca=0
    for i in range(1,m+1):
        temp=0
        if i%a==0:
            temp+=1
        if i%b==0:
            temp+=1
        if i%c==0 :
            temp+=1
        if temp==0:
            continue
        if i%a==0:
            al+=(6//temp)
        if i%b == 0:
            bo+=(6//temp)
        if i%c==0:
            ca+=(6//temp)
    print(*[al,bo,ca])
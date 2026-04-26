# 2203B. Beautiful Numbers
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[]
    a=0
    
    while n>0:
        temp=n%10
        arr.append(temp)
        n//=10
        a+=1
    sum1=arr.pop()
    a-=1
    arr.sort()
    for i in arr:
        if i+sum1<=9:
            sum1+=i
            a-=1
    print(a)

# H. Honey Cake


## incomplete
w,h,d=map(int,input().split())
n=int(input())
dw=[]
dh=[]
dd=[]
x=max(w,h,d)
for i in range(1,int(x**0.5)+1):
    if w%i==0:
        dw.append(i)
    if h%i==0:
        dh.append(i)
    if d%i==0:
        dd.append(i)

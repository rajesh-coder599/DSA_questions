# IPL and RCB

t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if y<x:
        print(x-y)
    else:
        print(0)
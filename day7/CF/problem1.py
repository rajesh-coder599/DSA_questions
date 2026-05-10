# 116A Tram

n=int(input())
capacity=0
curr_cap=capacity
for i in range(n):

    a,b=map(int,input().split())
    curr_cap+=(b-a)
    capacity=max(curr_cap,capacity)

print(capacity)
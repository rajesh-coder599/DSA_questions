# 2228B. Remilia Plays Soku


t=int(input())
for _ in range(t):
    n,x1,x2,k=map(int,input().split())
    forward=abs(x1-x2)
    backward=n-abs(x1-x2)
    if forward==backward:
        if k%2==0:
            print(forward)
        else:
            print(forward-1)
    elif forward>backward:
        
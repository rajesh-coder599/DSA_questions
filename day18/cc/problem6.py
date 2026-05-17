# Maximize Colours

t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    mx=0
    if x>0:
        mx+=1
        x-=1
    if y>0:
        mx+=1
        y-=1
    if z>0:
        mx+=1
        z-=1
    if z>x and z>y:
        if x>0 and z>0:
            mx+=1
            z-=1
            x-=1
        if y>0 and z>0:
            mx+=1
            y-=1
            z-=1
        if x>0 and y>0:
            mx+=1
            x-=1
            y-=1
    elif x>z and x>y:
        if x>0 and z>0:
            mx+=1
            z-=1
            x-=1
        if x>0 and y>0:
            mx+=1
            x-=1
            y-=1
        if y>0 and z>0:
            mx+=1
            y-=1
            z-=1
    else:
        if x>0 and y>0:
            mx+=1
            x-=1
            y-=1
        if y>0 and z>0:
            mx+=1
            y-=1
            z-=1
        if x>0 and z>0:
            mx+=1
            z-=1
            x-=1
    
    print(mx)
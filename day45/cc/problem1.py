# Chef Goes to the Cinema


t=int(input())
for _ in range(t):
    x=int(input())
    currtime=0
    prevstation=0
    currstation=0
    i=1
    while currstation<x:
        prevstation=currstation
        currstation+=i
        currtime+=1
        i+=1
    ans=currtime+min(abs(x-prevstation),abs(x-currstation))
    if abs(x-prevstation)<=abs(x-currstation):
        ans-=1
    print(ans)
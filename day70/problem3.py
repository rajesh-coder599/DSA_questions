# 2029. Stone Game IX



def stoneGameIX(stones):
    r0=0
    r1=0
    r2=0
    for i in stones:
        if i%3==0:
            r0+=1
        elif i%3==1:
            r1+=1
        else:
            r2+=1
    if r0%2==0:
        return r1>0 and r2>0
    return abs(r1-r2)>2
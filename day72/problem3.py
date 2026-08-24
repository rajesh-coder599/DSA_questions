# 1386. Cinema Seat Allocation



def maxNumberOfFamilies(n,reservedSeats):
    reserved={}
    for x,y in reservedSeats:
        if 2<=y<=5:
            if x not in reserved:
                reserved[x]=[1,0,0]
            else:
                reserved[x][0]=1
        if 6<=y<=9:
            if x not in reserved:
                reserved[x]=[0,0,1]
            else:
                reserved[x][2]=1
        if 4<=y<=7:
            if x not in reserved:
                reserved[x]=[0,1,0]
            else:
                reserved[x][1]=1
    ans=n*2
    for v in reserved.values():
        if sum(v)==3:
            ans-=2
        else:
            ans-=1
    return ans
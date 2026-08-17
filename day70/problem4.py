# 4024. Nearest Available Drone



def nearestDrone(drones,target):
    tx,ty=target[0],target[1]
    mndis=float("inf")
    idx=None
    n=len(drones)
    for i in range(n):
        x,y,r=drones[i]
        temp=abs(x-tx)+abs(y-ty)
        if temp<=r:
            if temp<mndis:
                mndis=temp
                idx=i
    if idx==None:
        return -1
    return idx
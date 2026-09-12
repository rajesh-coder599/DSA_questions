# 4045. Count Robot Groups



def countGroups(position,speed,distance):
    n=len(position)
    ans=n
    for i in range(n-2,-1,-1):
        if speed[i]>speed[i+1] or position[i+1]-position[i]<=distance:
            ans-=1
            speed[i]=speed[i+1]
    return ans
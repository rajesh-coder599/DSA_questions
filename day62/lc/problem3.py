# 4008. Minimum Initial Strength to Defeat All Monsters



def minInitialStrength(monsters,boosts):
    n=len(monsters)
    tempbonus=[0]*n
    for l,r,v in boosts:
        tempbonus[l]+=v
        if r<n-1:
            tempbonus[r+1]-=v
    bonus=[tempbonus[0]]
    for i in range(1,n):
        bonus.append(bonus[i-1]+tempbonus[i])
    ans=0
    currstrenght=0
    totalstrength=0
    for i in range(n):
        mon=monsters[i]
        b=bonus[i]
        if currstrenght+b>=mon:
            currstrenght-=mon
            if currstrenght<0:
                currstrenght=0
        else:
            ans=totalstrength+mon-currstrenght-b
            currstrenght=0
        totalstrength+=mon
    return ans
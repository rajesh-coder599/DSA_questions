# 1833. Maximum Ice Cream Bars



def maxIceCream(costs,coins):
    costs.sort()
    currsum=0
    ans=0
    for i in range(len(costs)):
        currsum+=costs[i]
        if currsum>coins:
            break
        ans+=1
    return ans
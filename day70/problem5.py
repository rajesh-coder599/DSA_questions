# 4020. Elevator Requests I



def elevatorRequests(n,requests):
    ans=0
    currfloor=0
    for i in requests:
        ans+=abs(i-currfloor)
        currfloor=i
    return ans
# Q1. Maximum Manhattan Distance After All Moves


def maxDistance(moves):
    freemove=0
    x=0
    y=0
    for i in moves:
        if i=="L":
            x-=1
        elif i=="R":
            x+=1
        elif i=="U" :
            y-=1
        elif i=="D" :
            y+=1
        else:
            freemove+=1
    if x>=0:
        x+=freemove
    else:
        x-=freemove
    return abs(x)+abs(y)
# Triangle Classification


def distance(x1,y1,x2,y2):
    return (x2-x1)**2+(y2-y1)**2
subtast_id=int(input())
t=int(input())
for _ in range(t):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=distance(x1,y1,x2,y2)
    b=distance(x2,y2,x3,y3)
    c=distance(x3,y3,x1,y1)
    if a!=b and a!=c and b!=c:
        ans="Scalene "
    else:
        ans="Isosceles "
    sides=[a,b,c]
    sides.sort()
    if subtast_id==2:

        if sides[0]+sides[1]==sides[2] :
            ans+="Right"
        elif sides[0]+sides[1]>sides[2] :
            ans+="Acute"
        else:
            ans+="Obtuse"

    print(ans,"triangle")
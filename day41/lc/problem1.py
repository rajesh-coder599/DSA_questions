# 1344. Angle Between Hands of a Clock


def angleClock(hour,minutes):
    a=hour*5+minutes/12
    b=abs(minutes-a)
    angle=b*6
    return min(angle,abs(angle-360))

# 1401. Circle and Rectangle Overlapping



def checkOverlap(radius,xCenter,yCenter,x1,y1,x2,y2):
    return max(x1,radius-xCenter)<min(x2,radius+xCenter) and max(y1,radius-yCenter)<min(y2,radius+yCenter)
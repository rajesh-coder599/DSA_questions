# Q1. Check Good Integer



def checkGoodInteger(n):
    s=str(n)
    digisum=0
    squareSum=0
    for i in s:
        digisum+=int(i)
        squareSum+=(int(i))**2
    if squareSum - digisum >= 50 :
        return True
    return False
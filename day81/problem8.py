# 4098. Minimize the Maximum Value of GCD-Connected Array




def minimumMaxValue(n,index,value):
    if value==1:
        return -1
    smallest_divisor=None
    for i in range(2,int(value**0.5)+1):
        if value%i==0:
            smallest_divisor=i
            break
    if smallest_divisor==None:
        smallest_divisor=value
    after=n-index-1
    before=n-after-1
    if value-smallest_divisor-2*(before-1)<=0:
        return -1
    if index==n-1:
        return value
    ans=value+smallest_divisor+2*(after-1)
    return ans
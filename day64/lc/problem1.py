# 3345. Smallest Divisible Digit Product I



def smallestNumber(n,t):
    while True:
        s=str(n)
        product=1
        for i in s:
            product*=int(i)
        if product%t==0:
            return n
        n+=1
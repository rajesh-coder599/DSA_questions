# 3483. Unique 3-Digit Even Numbers

# brute force
def totalNumbers(digits):
    n=len(digits)
    a=set()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and j!=k and i!=k:
                    digi=digits[i]*100+digits[j]*10+digits[k]
                    if digi%2==0 and digi not in a and digi>99:
                        a.add(digi)
    return len(a)
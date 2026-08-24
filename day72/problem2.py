# 3622. Check Divisibility by Digit Sum and Product



def checkDivisibility(n):
    digsum=0
    digproduct=1
    for i in str(n):
        digsum+=int(i)
        digproduct*=int(i)
    return n%(digproduct+digsum)==0
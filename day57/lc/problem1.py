# 3536. Maximum Product of Two Digits


def maxProduct(n):
    a=0
    b=0
    while n>0:
        x=n%10
        n//=10
        if x>=a:
            b=a
            a=x
        else:
            b=max(b,x)
    return a*b
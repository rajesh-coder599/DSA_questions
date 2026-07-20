# 1979. Find Greatest Common Divisor of Array


def findGCD(nums):
    a=min(nums)
    b=max(nums)
    while b!=0:
        a,b=b,a%b
    return a
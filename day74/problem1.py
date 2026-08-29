# 3718. Smallest Missing Multiple of K


def missingMultiple(nums,k):
    a=set(nums)
    x=k
    while x in a:
        x+=k
    return x
# 3513. Number of Unique XOR Triplets I


def uniqueXorTriplets(nums):
    n=len(nums)
    if n<3:
        return n
    return 2**(len(bin(n))-2)
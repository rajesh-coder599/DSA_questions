# 3514. Number of Unique XOR Triplets II


def uniqueXorTriplets(nums):
    a=set()
    n=len(nums)
    for i in range(n):
        for j in range(i,n):
            a.add(nums[i]^nums[j])
    b=set()
    for x in a:
        for y in nums:
            b.add(x^y)
    return len(b)
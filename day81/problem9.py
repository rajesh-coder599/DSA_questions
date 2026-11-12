# 453. Minimum Moves to Equal Array Elements



def minMoves(nums):
    n=len(nums)
    if n==1:
        return 0
    if n==2:
        return abs(nums[0]-nums[1])
    mn=min(nums)
    operations=sum(nums)-mn*n
    return operations
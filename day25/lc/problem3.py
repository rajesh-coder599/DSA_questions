# Q3. Minimum Operations to Sort a Permutation


def minOperations(nums):
    n=len(nums)
    ind=nums.index(0)
    backward=True
    forward=True

    for i in range(n-1):
        if nums[(i+ind)%n] +1!= nums[(i+ind+1)%n]:
            forward=False
            break
    
    for i in range(n,1,-1):
        if nums[(i+ind)%n] != nums[(i+ind-1)%n] - 1:
            backward=False
            break
    
    if forward:
        return min(ind,n-ind+2)
    if backward:
        return min(ind+2,n-ind)
    return -1

nums=[1,2,3,4,0]
print(minOperations(nums))
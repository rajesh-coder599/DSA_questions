# 4048. Count Values With Equally Spaced Occurrences I





def countSpecialIntegers(nums):
    from collections import defaultdict
    n=len(nums)
    ans=0
    idx=defaultdict(list)
    for i in range(n):
        idx[nums[i]].append(i)
    for v in idx.values():
        if len(v)!=3:
            continue
        x,y,z=v
        if y-x==z-y:
            ans+=1
    return ans
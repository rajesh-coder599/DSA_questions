# 4049. Count Values With Equally Spaced Occurrences II





def countSpecialIntegers(nums):
    from collections import defaultdict
    n=len(nums)
    ans=0
    idx=defaultdict(list)
    for i in range(n):
        idx[nums[i]].append(i)
    for v in idx.values():
        l=len(v)
        if l<3:
            continue
        perv=v[1]
        diff=v[1]-v[0]
        check=True
        for x in range(2,l):
            if v[x]-perv!=diff:
                check=False
                break
            perv=v[x]
        if check:
            ans+=1
    return ans
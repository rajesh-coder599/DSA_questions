# 128. Longest Consecutive Sequence


def longestConsecutive(nums):
    parent={}
    a=set(nums)
    vis=set()
    ans=0
    for i in set(nums):
        if i in vis:
            continue
        currlen=0
        x=i
        while x in a and x not in vis:
            vis.add(x)
            currlen+=1
            x-=1
        if x in vis:
            currlen+=parent[x]
        parent[i]=currlen
        ans=max(ans,currlen)
    return ans
        

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
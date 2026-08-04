# 3731. Find Missing Elements



def findMissingElements(nums):
    ans=[]
    a=set(nums)
    for i in range(min(nums),max(nums)):
        if i not in a:
            ans.append(i)
    return ans
# 525. Contiguous Array


from collections import defaultdict
def findMaxLength(nums):
    n=len(nums)
    currsum=0
    equalfreq=defaultdict(list)
    for i in range(n):
        x=nums[i]
        if x==1:
            currsum+=1
        else:
            currsum-=1
        equalfreq[currsum].append(i)
    ans=0
    for k,v in equalfreq.items():
        if k==0:
            ans=max(ans,v[-1]+1)
        a=v[0]
        b=v[-1]
        ans=max(ans,b-a)
    return ans
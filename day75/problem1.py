# 2091. Removing Minimum and Maximum From Array



def minimumDeletions(nums):
    n=len(nums)
    mn=min(nums)
    mx=max(nums)
    mnidx=None
    mxidx=None
    for i in range(n):
        if nums[i]==mn:
            mnidx=i
        if nums[i]==mx:
            mxidx=i
    a=max(mnidx,mxidx)+1
    b=n-min(mnidx,mxidx)
    c=min(mnidx,mxidx)+1+n-max(mnidx,mxidx)
    return min(a,b,c)
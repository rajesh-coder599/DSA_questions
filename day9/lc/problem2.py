# 3708. longest fibonacci subarray

nums=[5,2,7,9,16]
def lfs(nums):
    n=len(nums)
    if n<=2:
        return n
    mxlen=2
    currlen=2
    for i in range(2,n):
        if nums[i-1]+nums[i-2]==nums[i]:
            currlen+=1
            mxlen=max(mxlen,currlen)
        else:
            currlen=2
    return mxlen

print(lfs(nums))
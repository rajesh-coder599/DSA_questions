# 3994. Minimum Adjacent Swaps to Partition Array



def minAdjacentSwaps(nums,a,b):
    n=len(nums)
    ans1=0
    l=0
    r=n-1
    t=0
    for i in nums[::-1]:
        if i<=b:
            break
        r-=1
    for i in range(n):
        if nums[i]<a:
            ans1+=i-l-t
            l+=1
        if nums[i]>b and i<r:
            ans1+=r-i
            r-=1
            t+=1
    return ans1
a=4
b=8
nums=[3,7,5,9]
print(minAdjacentSwaps(nums,a,b))
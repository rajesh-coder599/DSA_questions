# 4011. Count Subarrays With Even Odd Ratio I



def countRatioSubarrays(nums,a,b):
    n=len(nums)
    ans=0
    for i in range(n):
        x=0
        y=0
        for j in range(i,n):
            if nums[j]%2==0:
                x+=1
            else:
                y+=1
            if y!=0 and x/y<=a/b:
                ans+=1
    return ans
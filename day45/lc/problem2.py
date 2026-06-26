# 3737. Count Subarrays With Majority Element I



def countMajoritySubarrays(nums,target):
    ans=0
    n=len(nums)
    for i in range(n):
        targetfreq=0
        currlen=0
        for j in range(i,n):
            x=nums[j]
            if x==target:
                targetfreq+=1
            else:
                currlen+=1
            if targetfreq>currlen:
                ans+=1
    return ans
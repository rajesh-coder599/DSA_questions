# Q2. Valid Subarrays With Matching Sum Digits I



def countValidSubarrays(nums,x):
    n=len(nums)
    ans=0
    for i in range(n):
        temp=0
        currsum=0
        for j in range(i,n):
            currsum+=nums[j]
            s=str(currsum)
            if int(s[0])==x and int(s[-1])==x:
                temp+=1
        ans+=temp
    return temp
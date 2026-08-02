# 4010. Maximize Pair Strength Using GCD




def maxPairStrength(nums):
    n=len(nums)
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    ans=1
    for i in range(n):
        x=nums[i]
        for j in range(i+1,n):
            y=nums[j]
            temp=x*y
            temp//=gcd(x,y)
            ans=max(ans,temp)
    return ans
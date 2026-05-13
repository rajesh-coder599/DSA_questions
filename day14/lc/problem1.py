# 1674. Minimum Moves to Make Array Complementary


nums=[28,50,76,80,64,30,32,84,53,8]
limit=84
def minMoves(nums, limit):
    n=len(nums)
    z=float("inf")
    for i in range(n//2):
        a=nums[i]+nums[n-i-1]
        ans=0
        for i in range(n//2):
            temp=nums[i]+nums[n-i-1]
            # equal
            if temp==a:
                continue
            # greater
            if temp>a:
                # +1 condition
                if 1+nums[n-i-1]<=a or nums[i]+1<=a:
                    ans+=1
                # +2 condition
                else:
                    ans+=2
            # lessthen
            elif temp<a:
                # +1 condition
                if limit+nums[n-i-1]>=a or nums[i]+limit>=a:
                    ans+=1
                # +2 condition
                else:
                    ans+=2
        z=min(z,ans)
    return z

print(minMoves(nums,limit))
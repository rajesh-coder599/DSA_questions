# 3927. Minimize Array Sum Using Divisible Replacements

def minArraySum(nums):
    a=set(nums)
    ans=0
    for i in nums:
        temp=[i]
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                if j in a:
                    temp.append(j)
                elif j!=1 and i//j in a:
                    temp.append(i//j)
        ans+=min(temp)
    return ans

nums=[4,2,8,3]
print(minArraySum(nums))
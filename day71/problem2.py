# 2913. Subarrays Distinct Element Sum of Squares I



def sumCounts(nums):
    n=len(nums)
    ans=0
    for i in range(n):
        temp=set()
        k=0
        for j in range(i,n):
            if nums[j] not in temp:
                temp.add(nums[j])
                k+=1
                ans+=k*k
    return ans
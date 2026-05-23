# biweekly contest 183
# Q2. Minimum Operations to Make Array Modulo Alternating I

def minOperations(nums,k):
    n=len(nums)
    ans=float("inf")

    for x in range(k):

        for y in range(k):
            if y==x:
                continue
            temp_ans=0
            for i in range(n):
                if i%2==0:
                    temp=nums[i]%k
                    if temp!=x:
                        temp_ans+=min(abs(temp-x),k-abs(temp-x))
                if i%2 != 0:
                    temp=nums[i]%k
                    if temp != y :
                        temp_ans+=min(abs(temp-y),k-abs(temp-y))
            ans=min(ans,temp_ans)

    return ans

k=4
nums=[63,36,77,19]
print(minOperations(nums,k))
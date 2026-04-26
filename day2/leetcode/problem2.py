# 3909. Compare Sums of Bitonic Parts


nums = [1,3,2,1]
n=len(nums)
i=0
while i!=n:
    if nums[i]>nums[i+1]:
        break
    i+=1
sum1=sum(nums[0:i+1])
sum2=sum(nums[i:n])
if sum1>sum2:
    print(0)
elif sum1<sum2:
    print(1)
else:
    print(-1)
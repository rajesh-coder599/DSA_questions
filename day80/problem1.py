# 3886. Sum of Sortable Integers



def sortableIntegers(nums):
    from collections import defaultdict
    n=len(nums)
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    sorted_arr=sorted(nums)
    ans=0
    for i in divisors:
        check=True
        for j in range(0,n,i):
            freq=defaultdict(int)
            c=0
            for k in range(i):
                freq[nums[k+j]]+=1
                freq[sorted_arr[k+j]]-=1
                if nums[k+j]>nums[(k+1)%i+j]:
                    c+=1
                    if c>1:
                        check=False
                        break
            if check==False:
                break
            for v in freq.values():
                if v!=0:
                    check=False
                    break
        if check:
            ans+=i
    return ans
arr=[1,2]
print(sortableIntegers(arr))
# 3020. Find the Maximum Number of Elements in Subset


from collections import defaultdict
def maximumLength(nums):
    freq=defaultdict(int)
    for i in nums:
        if i != 1:
            freq[i]+=1
    ans=1
    x=nums.count(1)
    ans=max(ans,x-(1 if x%2==0 else 0))
    for k,v in freq.items():
        temp=0
        check=True
        while k in freq:
            if freq[k]>=2 :
                temp+=2
            else:
                temp+=1
                check=False
                break
            k=k*k
        if check:
            temp-=1
        ans=max(ans,temp)
    return ans
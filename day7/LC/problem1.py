# 3712 sum of elements with frequency divisible by k

nums=[1,2,2,3,3,3,3,4]
k=2
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

ans=0
for key,val in freq.items():
    if val%k==0:
        ans+=(key*val)

print(ans)
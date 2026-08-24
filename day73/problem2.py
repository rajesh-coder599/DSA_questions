# 4032. Longest Subarray With at Most K Distinct Prime Factors



## incomplete code!!
def longestSubarray(nums,k):
    prime={}
    n=len(nums)
    for i in nums:
        temp=i
        s=set()
        a=2
        while a*a<=i:
            while i%a==0:
                s.add(a)
                i//=a
            a+=1
        if i>1:
            s.add(a)
        prime[temp]=s
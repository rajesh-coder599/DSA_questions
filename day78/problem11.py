# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum




def minSumOfLengths(arr,target):
    n=len(arr)
    first=[float("inf")]*(n+1)
    second=float("inf")
    prev=0
    curr_sum=0
    for i in range(n):
        curr_sum+=arr[i]
        while curr_sum>target:
            curr_sum-=arr[prev]
            prev+=1
        first[i+1]=first[i]
        if curr_sum==target:
            l=i-prev+1
            if first[prev]!=float("inf"):
                second=min(second,first[prev]+l)
            first[i+1]=min(first[i+1],l)
    if second==float("inf"):
        return -1
    return second

a=[3,2,2,4,3]
t=3
print(minSumOfLengths(a,t))
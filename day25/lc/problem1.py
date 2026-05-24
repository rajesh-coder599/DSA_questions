
# Q1. Limit Occurrences in Sorted Array©leetcode


def limitOccurrences(nums,k):
    n=len(nums)
    count=1
    curr_ch=nums[0]
    a=[nums[0]]
    for i in range(1,n):
        if nums[i]==curr_ch and count<k:
            a.append(nums[i])
            count+=1
        elif nums[i] != curr_ch:
            count=1
            curr_ch=nums[i]
            a.append(nums[i])
    
    return a

nums=[1,1,1,1,2,2,3]
k=2
print(limitOccurrences(nums,k))
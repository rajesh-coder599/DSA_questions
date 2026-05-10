# 3920 maximize fized points after deletions

import heapq
nums=[1,0,6,1,2,8,7,4,3]

min_heap=[]
n=len(nums)
for i in range(n):
    if nums[i]<=i:
        heapq.heappush(min_heap,[i-nums[i],nums[i]])

#LIS

def lowerbound(arr,target):
    n=len(arr)
    l=0
    r=n-1
    ans=n
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<target:
            l=mid+1
        else:
            ans=mid
            r=mid-1

    return ans

lis=[]
lis.append(min_heap[0][1])
for i in range(1,len(min_heap)):
    a=min_heap[i][1]
    if lis[-1]<a:
        lis.append(a)
    else:
        temp=lowerbound(lis,a)
        lis[temp]=a

print(len(lis))
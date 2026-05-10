# 2227F. it just keeps going sideways


def lowerbound(nums,target):
    n=len(nums)
    l=0
    r=n-1
    ans=0
    while l<=r:
        mid=(l+r)//2
        if nums[mid]>=target:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    s_arr=arr.copy()
    s_arr.sort()
    carry=0
    for i in range(n):
        diff=(arr[i]+carry-s_arr[i])
        carry=diff
        ans+=diff
    mx=0
    for i in range(n):
        if arr[i]<=s_arr[i] :
            lb=lowerbound(s_arr,arr[i])
            mx=max(mx,i-lb)
    print(ans+mx)
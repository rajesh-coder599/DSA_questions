# 4013. Count Subarrays With Even Odd Ratio II




def countRatioSubarrays(nums,a,b):
    ans=0
    def mergesort(pre,l,r):
        nonlocal ans
        if l>=r :
            return
        mid=(l+r)//2
        mergesort(pre,l,mid)
        mergesort(pre,mid+1,r)
        i=l
        j=mid+1
        while i<=mid and j<=r :
            if pre[i]>=pre[j]:
                ans+=(mid-i+1)
                j+=1
            else:
                i+=1
        i=l
        j=mid+1
        temp=[]
        while i<=mid and j<=r:
            if pre[i]<=pre[j] :
                temp.append(pre[i])
                i+=1
            else:
                temp.append(pre[j])
                j+=1
        while i<=mid:
            temp.append(pre[i])
            i+=1
        while j<=r:
            temp.append(pre[j])
            j+=1
        for k in range(l,r+1):
            pre[k]=temp[k-l]
    n=len(nums)
    x=0
    y=0
    perfix=[0]
    for i in range(n):
        if nums[i]%2==0:
            x+=1
        else:
            y+=1
        perfix.append(b*x-a*y)
    mergesort(perfix,0,n)
    return ans
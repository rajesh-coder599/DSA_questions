# 2948. Make Lexicographically Smallest Array by Swapping Elements




def lexicographicallySmallestArray(nums,limit):
    n=len(nums)
    arr=sorted(nums)
    groups=[]
    group=[arr[-1]]
    for i in range(n-2,-1,-1):
        if arr[i+1]-arr[i]<=limit:
            group.append(arr[i])
        else:
            groups.append(group)
            group=[arr[i]]
    groups.append(group)
    nameofgroup={}
    groupmemberof={}
    currname=0
    for g in groups:
        nameofgroup[currname]=g
        for i in g:
            groupmemberof[i]=currname
        currname+=1
    ans=[]
    for i in nums:
        ans.append(nameofgroup[groupmemberof[i]].pop())
    return ans
arr=[1,7,6,18,2,1]
l=3
print(lexicographicallySmallestArray(arr,l))
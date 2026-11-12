# 2089. Find Target Indices After Sorting Array



def targetIndices(nums,target):
    ans=[]
    c=0
    freq=0
    for i in nums:
        if i<target:
            c+=1
        elif i==target:
            freq+=1
    for i in range(c,freq+c+1):
        ans.append(i)
    return ans
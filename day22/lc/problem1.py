# 3043. Find the Length of the Longest Common Prefix


def longestCommonPrefix(arr1,arr2):
    prefix=set()

    for i in arr1:
        a=str(i)
        prefix.add(int(a[0]))
        for j in range(1,len(a)+1):
            temp=a[:j]
            prefix.add(int(temp))

    ans=0

    for i in arr2:
        a=str(i)
        if int(a[0]) in prefix:
            ans=max(ans,1)
        for j in range(1,len(a)+1):
            temp=a[:j]
            if int(temp) in prefix:
                ans=max(ans,len(temp))
    
    return ans


arr1 = [1,10,100]
arr2 = [1000]
print(longestCommonPrefix(arr1,arr2))
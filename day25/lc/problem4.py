

# Q4. Number of Pairs After Increment


def numberOfPairs(nums1,nums2,queries):
    a={}
    for i in nums1:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    b={}
    for i in nums2:
        if i in b:
            b[i]+=1
        else:
            b[i]=1

    
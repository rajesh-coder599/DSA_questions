# 2540. Minimum Common Value


def getCommon(nums1, nums2):
    n1=len(nums1)
    n2=len(nums2)

    i=0
    j=0
    while i<n1 and j<n2 :
        if nums1[i]>nums2[j]:
            j+=1
        elif nums2[j]>nums1[i]:
            i+=1
        else:
            return nums1[i]
        
    
    return -1

nums1 = [1,2,3]
nums2 = [2,3,4,5]
print(getCommon(nums1,nums2))
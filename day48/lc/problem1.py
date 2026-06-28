# 1846. Maximum Element After Decreasing and Rearranging



def maximumElementAfterDecrementingAndRearranging(arr):
    arr.sort()
    n=len(arr)
    arr[0]=1
    for i in range(1,n):
        x=abs(arr[i-1]-arr[i])
        if x>1:
            arr[i]-=(x-1)
    return max(arr)
# 315. Count of Smaller Numbers After Self



def countSmaller(nums):
    n=len(nums)
    ans=[0]*n
    vals=list(enumerate(nums))
    def merge(left,right):
        result=[]
        i=j=0
        while i<(len(left)) and j<(len(right)):
            if left[i][1]<=right[j][1]:
                ans[left[i][0]]+=j
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<len(left):
            ans[left[i][0]]+=j
            result.append(left[i])
            i+=1
        while j<(len(right)):
            result.append(right[j])
            j+=1
        return result
    def merge_sort(arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=merge_sort(arr[:mid])
        right=merge_sort(arr[mid:])
        return merge(left,right)
    merge_sort(vals)
    return ans

nums = [5,2,6,1]
print(countSmaller(nums))
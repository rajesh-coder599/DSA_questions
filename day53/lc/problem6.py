# 3994. Minimum Adjacent Swaps to Partition Array



def minAdjacentSwaps(nums,a,b):
    p2=0
    p3=0
    swap=0
    for i in nums:
        if i<a:
            swap+=p2+p3
        elif i<b:
            swap+=p3
            p2+=1
        else:
            p3+=1
    return swap

arr=[5,2,6,1]
a=3
b=4
print(minAdjacentSwaps(arr,a,b))
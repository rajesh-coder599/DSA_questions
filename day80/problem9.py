# 4093. Maximize Sum After At Most K Digit Rearrangements





def maximizeSum(nums,k):
    rearrenged_int=[]
    for num in nums:
        temp=[]
        x=num
        while x>0:
            temp.append(x%10)
            x//=10
        temp.sort(reverse=True)
        a=0
        for i in temp:
            a=a*10+i
        if a==num:
            continue
        rearrenged_int.append(a-num)
    s=sum(nums)
    rearrenged_int.sort(reverse=True)
    for i in range(min(k,len(rearrenged_int))):
        s+=rearrenged_int[i]
    return s
arr=[26,6,37,41,27,29]
x=2
print(maximizeSum(arr,x))
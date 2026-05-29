# 3300. Minimum Element After Replacement With Digit Sum


def minElement(nums):
    currmn=float("inf")
    for i in nums:
        a=str(i)
        temp=0
        for j in a:
            temp+=int(j)
        currmn=min(currmn,temp)
    return currmn
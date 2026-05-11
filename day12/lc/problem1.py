# 2553. Separate the Digits in an Array

def separateDigits(nums):
    ans=[]
    for i in nums:
        a=str(i)
        for j in a:
            ans.append(int(j))

    return ans

nums=[12,13,14,15]
print(separateDigits(nums))
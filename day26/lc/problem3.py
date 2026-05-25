# 45. Jump Game II


def jump(nums):
    n=len(nums)

    jump=0
    far=0
    end=0
    for i in range(n-1):
        far=max(far,i+nums[i])

        if i==end:
            jump+=1
            end=far
    
    return jump

nums=[2,3,0,1,4]
print(jump(nums))
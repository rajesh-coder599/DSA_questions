# 55. Jump Game


def canJump(nums):
    n=len(nums)

    mx=0
    for i in range(n):
        if i>mx:
            return False
        mx=max(mx,i+nums[i])

    return True

nums = [2,3,1,1,4]
print(canJump(nums))
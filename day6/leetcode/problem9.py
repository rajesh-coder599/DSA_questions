# weekly contest 500 Q1

# count indices with oposite parity
nums=[1,2,3,4]

n=len(nums)
ans=[0]*n
curr_odd=0
curr_even=0
for i in range(n-1,-1,-1):
    if nums[i]%2==0:
        curr_even+=1
        ans[i]=curr_odd
    else:
        curr_odd+=1
        ans[i]=curr_even

print(ans)
# weekly contest 500 Q3

# minimum cost to move between indieces

nums=[-5,-2,3]
queries=[[0,2],[2,0],[1,2]]

n=len(nums)
closest=[0]*n
closest[0]=nums[1]
closest[-1]=nums[-2]
for i in range(1,n-1):
    if abs(nums[i-1]-nums[i])<abs(nums[i+1]-nums[i]):
        closest[i]=(nums[i-1])
    elif abs(nums[i-1]-nums[i])>abs(nums[i+1]-nums[i]):
        closest[i]=(nums[i+1])
    else:
        closest[i]=(min(nums[i-1],nums[i+1]))

prefix_dis=[0]*n
sufix_dis=[0]*n
for i in range(1,n):
    if nums[i]==closest[i-1]:
        prefix_dis[i]=1
    else:
        prefix_dis[i]=abs(nums[i-1]-nums[i])

for i in range(n-2,-1,-1):
    if nums[i]==closest[i+1] :
        sufix_dis[i]=1
    else:
        sufix_dis[i]=abs(nums[i+1]-nums[i])

prefix_sum=[0]*n
prefix_sum[0]=prefix_dis[0]
for i in range(1,n):
    prefix_sum[i]=prefix_sum[i-1]+prefix_dis[i]

sufix_sum=[0]*n
sufix_sum[-1]=sufix_dis[-1]
for i in range(n-2,-1,-1):
    sufix_sum[i]=sufix_sum[i+1]+sufix_dis[i]
    
ans=[]
for li,ri in queries:
    if li>ri:
        ans.append(sufix_sum[ri]-sufix_sum[li])
    elif li<ri:
        ans.append(prefix_sum[ri]-prefix_sum[li])
    else:
        ans.append(0)

print(ans)
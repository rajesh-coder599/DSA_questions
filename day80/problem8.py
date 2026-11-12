# 4094. Count Frequency Staircase Subarrays I




def countStaircase(nums):
    n=len(nums)
    ans=n
    for i in range(n):
        freq={}
        distict_num=set()
        remain=0
        for j in range(i,n):
            distict_num.add(nums[j])
            if nums[j] in freq:
                freq[nums[j]]=[1+freq[nums[j]][0],freq[nums[j]][1]]
                remain-=1
                if freq[nums[j]][0]>freq[nums[j]][1]:
                    break
                elif freq[nums[j]][0]==freq[nums[j]][1] and remain==0:
                    ans+=1
            else:
                freq[nums[j]]=[1,len(distict_num)]
                remain+=len(distict_num)-1
    return ans
arr=[5,8,8,2,2,2]
print(countStaircase(arr))
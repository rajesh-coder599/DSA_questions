# 3551. Minimum Swaps to Sort by Digit Sum



def minSwaps(nums):
    digi_sum=[]
    n=len(nums)
    for i in range(n):
        d=nums[i]
        temp=0
        x=d
        while d>0:
            temp+=d%10
            d//=10
        digi_sum.append((x,temp,i))
    digi_sum.sort(key=lambda x: (x[1],x[0]))
    swap=0
    visited=[False]*n
    for i in range(n):
        if visited[i] or digi_sum[i][2]==i:
            continue
        j=i
        cycle_size=0
        while not visited[j]:
            visited[j]=True
            cycle_size+=1
            j=digi_sum[j][2]
        swap+=cycle_size-1
    print(digi_sum)
    return swap

arr=[268835996,65052660,415128775]
print(minSwaps(arr))
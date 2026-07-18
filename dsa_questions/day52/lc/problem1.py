# 3867. Sum of GCD of Formed Pairs

def gcdSum(nums):
    def gcd(x,y):
        while y!=0:
            x,y=y,x%y
        return x
    currmx=nums[0]
    perfectgcd=[]
    for i in nums:
        currmx=max(currmx,i)
        perfectgcd.append(gcd(currmx,i))
    perfectgcd.sort()
    l=0
    r=len(perfectgcd)-1
    ans=0
    while l<r:
        ans+=gcd(perfectgcd[l],perfectgcd[r])
        l+=1
        r-=1
    return ans
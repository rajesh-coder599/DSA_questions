# 4021. Minimum Operations to Make a Rotated Palindrome I



def minOperations(s):
    n=len(s)
    ans=float("inf")
    for i in range(n):
        temp=s[i:]+s[:i]
        l=0
        r=n-1
        oprations=i
        while l<=r:
            a=ord(temp[l])-96
            b=ord(temp[r])-96
            oprations+=min(abs(a-b),26-max(a,b)+min(a,b))
            l+=1
            r-=1
        ans=min(ans,oprations)
    return ans
# Q1. Sum of Compatible Numbers in Range I©leetcode


def sumOfGoodIntegers(n,k):
    ans=0
    for i in range(max(1,n-k),n+k+1):
        if i&n==0:
            ans+=i
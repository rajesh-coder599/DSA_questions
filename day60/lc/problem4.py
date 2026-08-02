# 4006. Count Valid Prefixes



def countValidPrefixes(s):
    zeros=0
    ones=0
    ans=0
    for i in s:
        if i=="0":
            zeros+=1
        else:
            ones+=1
        if abs(zeros-ones)<=1:
            ans+=1
    return ans
# 3998. Transform Binary String Using Subsequence Sort



def transformStr(s,strs):
    n=len(s)
    ans=[]
    onesofs1=s.count("1")
    zerosofs1=s.count("0")
    for s2 in strs:
        ones=s2.count("1")
        zeros=s2.count("0")
        if ones>onesofs1 or zeros>zerosofs1:
            ans.append(False)
            continue
        count1=0
        count2=0
        check=True
        for i in range(n):
            a=s[i]
            b=s2[i]
            if b=="?" :
                if zeros<zerosofs1:
                    zeros+=1
                    b="0"
                else:
                    b="1"
            if a=="1":
                count1+=1
            if b=="1":
                count2+=1
            if count2>count1:
                check=False
                break
        ans.append(check)
    return ans
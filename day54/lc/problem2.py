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
        t=0
        check=True
        for i in range(n):
            if s[i]==s2[i]:
                continue
            elif s[i]=="1" and s2[i]=="0":
                t+=1
            elif s[i]=="0" and s2[i]=="1":
                t-=1
                if t<0:
                    check=False
                    break
            elif s2[i]=="?" and t>0:
                t-=1
            elif s2[i]=="?" and s[i]==1 and t==0:
                t+=1
        if t>0:
            check=False
        ans.append(check)
    return ans

s="1100"
strs=["0011","11?1","1?1?"]
print(transformStr(s,strs))
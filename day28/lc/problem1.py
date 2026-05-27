# 3121. Count the Number of Special Characters II



def numberOfSpecialChars(word):
    n=len(word)
    if n==1 :
        return 0
    lower_al=set()
    upper_al=set()
    check=set()
    ans=0
    for i in word:
        if i.islower():
            if i not in check:
                if i in lower_al and i.upper() in upper_al:
                    ans-=1
                    check.add(i)
                if i.upper() in upper_al and i not in lower_al:
                    check.add(i)
            lower_al.add(i)
        else:
            temp=i.lower()
            if temp in lower_al and i not in upper_al:
                ans+=1
            upper_al.add(i)
    return ans

s="cADEDee"
print(numberOfSpecialChars(s))
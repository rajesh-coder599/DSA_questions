# 3992. Rearrange String to Avoid Character Pair



def rearrangeString(s,x,y):
    ans=""
    count=0
    for i in s:
        if i !=y:
            ans+=i
        else:
            count+=1
    temp=y*count
    return ans+temp
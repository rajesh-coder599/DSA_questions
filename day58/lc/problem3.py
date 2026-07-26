# 4000. Largest Integer With Given Digit Sum




def largestInteger(n,s):
    if s>=9:
        ans="9"*(s//9)
    else:
        ans=""
    s%=9
    if s>0:
        ans+=str(s)
    if len(ans)>n:
        return -1
    return int(ans+"0"*(n-len(ans)))
    
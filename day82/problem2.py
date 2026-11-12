# 4104. Count Valid Substrings II



def countValidSubstrings(s):
    n=len(s)
    if n<=2:
        return 3**(n-1)
    idxa=[-1]*n
    b=-1
    i=0
    ans=0
    for j in range(n):
        if s[j]=="a":
            idxa[j]=j
        else:
            idxa[j]=idxa[j-1]
        if s[j]=="b":
            b=j
        if s[j]=="c" and b!=-1 and idxa[b]!=-1:
            i=idxa[b]+1
        ans+=j-i+1
    return ans
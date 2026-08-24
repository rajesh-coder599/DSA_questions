# 4030. Check ASCII Palindromic




def isPalindromic(s):
    new_s=""
    for i in s:
        x=ord(i)
        temp=bin(x)
        new_s+="0"+temp[2:]
    l=0
    r=len(new_s)-1
    while l<=r:
        if new_s[l]!=new_s[r]:
            return False
        l+=1
        r-=1
    return True
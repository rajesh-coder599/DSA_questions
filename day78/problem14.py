# 32. Longest Valid Parentheses



def longestValidParentheses(s):
    l=r=mxln=0
    for i in s:
        if i=="(":
            l+=1
        else:
            r+=1
        if l==r:
            mxln=max(mxln,l+r)
        if r>l:
            l=r=0
    l=r=0
    for i in s[::-1]:
        if i=="(":
            l+=1
        else:
            r+=1
        if l==r:
            mxln=max(mxln,l+r)
        if l>r:
            l=r=0
    return mxln
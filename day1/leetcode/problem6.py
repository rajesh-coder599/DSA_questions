# 5. Longest Palindromic Substring

s = "babad"
n=len(s)
ps=s[0]
for i in range(n):
    l=i
    r=i
    while l>0 and r<n-1 :
        if s[l-1]==s[r+1]:
            l-=1
            r+=1
        else:
            break
    if r-l+1>len(ps) :
        ps=s[l:r+1]
    l=i
    r=i+1
    while l>=0 and r<=n-1:
        if s[l]==s[r]:
            if r-l+1>len(ps) :
                ps=s[l:r+1]
            l-=1
            r+=1
        else:
            break

print(ps)
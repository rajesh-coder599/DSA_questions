# 1358. Number of Substrings Containing All Three Characters



def numberOfSubstrings(s):
    n=len(s)
    ans=0
    k=0
    for i in range(n-2):
        if s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1] != s[i+2] :
            x=n-3-k
            y=(i-k)*(x-i)
            ans+=(x+y+1)
            k+=1
    return ans
# 3302. Find the Lexicographically Smallest Valid Sequence



def validSequence(word1,word2):
    n=len(word1)
    m=len(word2)
    suf=[-1]*m
    j=m-1
    for i in range(n-1,-1,-1):
        if j>=0 and word1[i]==word2[j]:
            suf[j]=i
            j-=1
    ans=[]
    skip=False
    j=0
    for i,c in enumerate(word1):
        if j==m:
            break
        if (c==word2[j] or not skip) and (j==m-1 or suf[j+1]>i):
            skip=(c!=word2[j])
            ans.append(i)
            j+=1
    return ans if j==m else []
# 3999. Minimum Number of String Groups Through Transformations



def minimumGroups(words):
    groups=set()
    def mnstr(s):
        s2=s+s
        n=len(s)
        i=0
        j=1
        k=0
        while i<n and j<n and k<n :
            if i==j:
                j+=1
            elif s2[i+k]==s2[j+k]:
                k+=1
            elif s2[i+k]>s2[j+k]:
                i=i+k+1
                k=0
            else:
                j=j+k+1
                k=0
        idx=min(i,j)
        return s[idx:]+s[:idx]
    for strs in words:
        evenstr=strs[::2]
        oddstr=strs[1::2]
        e1=mnstr(evenstr)
        o1=mnstr(oddstr)
        groups.add((e1,o1))
    return len(groups)

words = ["ntgwz","zwntg"]
print(minimumGroups(words))
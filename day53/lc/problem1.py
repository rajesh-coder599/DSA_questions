# 1081. Smallest Subsequence of Distinct Characters



def smallestSubsequence(s):
    from collections import defaultdict
    freq=defaultdict(int)
    al=set()
    for i in s:
        freq[i]+=1
        al.add(i)
    al=list(al)
    al.sort()
    name={}
    valofname={}
    for i in range(len(al)):
        name[al[i]]=i
        valofname[i]=al[i]
    ans=""
    vis=set()
    for i in s:
        if i in vis:
            freq[i]-=1
            continue
        elif freq[i]==1:
            ans+=i
            freq[i]-=1
            vis.add(i)
        elif name[i]-1 in valofname and freq[valofname[name[i]-1]]>0 :
            freq[i]-=1
        else:
            ans+=i
            freq[i]-=1
            vis.add(i)
    return ans
s="cbacdcbc"
print(smallestSubsequence(s))
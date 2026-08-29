# 3720. Lexicographically Smallest Permutation Greater Than Target


def lexGreaterPermutation(s,target):
    from collections import defaultdict
    n=len(s)
    freq=defaultdict(int)
    for i in s:
        freq[i]+=1
    arr=[]

    for i in range(n):
        used=defaultdict(int)
        check=False
        temp=""
        for x in range(i+1):
            ch=None
            for k,v in freq.items():
                if x<i:
                    if k==target[x] and v>used[k]:
                        ch=k
                        break
                elif x==i:
                    if k>target[x] and v>used[k]:
                        if ch==None:
                            ch=k
                        else:
                            ch=min(ch,k)
            if ch==None:
                check=True
                break
            else:
                temp+=ch
                used[ch]+=1
        if check:
            continue
        for k,v in sorted(freq.items()):
            if v>used[k]:
                temp+=k*(v-used[k])
        arr.append(temp)
    arr.sort()
    if len(arr)==0:
        return ""
    return arr[0]
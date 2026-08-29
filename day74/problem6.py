# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target



def lexPalindromicPermutation(s,target):
    from collections import defaultdict
    n=len(s)
    freq=defaultdict(int)
    for i in s:
        freq[i]+=1
    odd_count=0
    odd_ch=None
    for k,v in freq.items():
        if v%2!=0:
            odd_count+=1
            odd_ch=k
    if odd_count>1:
        return ""
    possible_str=[]
    l=n//2+1
    for i in range(l):
        check=False
        new_s=""
        used=defaultdict(int)
        for x in range(i+1):
            ch=None
            temp=False
            # if n%2!=0 and x==l-1:
            #     continue
            if x==n//2:
                continue
            for k,v in freq.items():
                if x==i:
                    if used[k]<v//2 and k>target[x]:
                        if ch==None:
                            ch=k
                        else:
                            ch=min(ch,k)
                elif x<i:
                    if used[k]<v//2 and k==target[x]:
                        ch=k
                        break
            if ch==None:
                check=True
                break
            new_s+=ch
            used[ch]+=1
        if check:
            continue
        for k,v in sorted(freq.items()):
            if used[k]<v//2:
                new_s+=k*((v//2)-used[k])
        temp=new_s[::-1]
        if odd_ch==None:
            possible_str.append(new_s+temp)
        else:
            possible_str.append(new_s+odd_ch+temp)
    possible_str.sort()
    for i in possible_str:
        if i>target:
            return i
    return ""

s="bb"
t="ba"
print(lexPalindromicPermutation(s,t))
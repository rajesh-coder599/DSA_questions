# 3926. Count Valid Word Occurrences

def countWordOccurrences(chunks, queries):
    s="".join(chunks)
    arr=s.split("--")
    for i in arr:
        if " " in i:
            x=i.split()
            arr+=x
    freq={

    }
    for i in arr:
        a=i
        if a[-1]=="-" or a[0]=="-":
            if len(a)==1:
                continue
            if a[-1]=="-":
                a=a[:-1]
            if a[0]=="-":
                a=a[1:]
        if a in freq:
            freq[a]+=1
        else:
            freq[a]=1
        

    ans=[]
    for i in queries:
        if i in freq:
            ans.append(freq[i])
        else:
            ans.append(0)
    print(freq)
    return ans

chunks = ["x--hp m-ym - -lf- "]
queries = ["m-ymj","x","m-ym","hp","lf"]
print(countWordOccurrences(chunks,queries))
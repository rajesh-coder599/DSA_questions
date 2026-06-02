


def digitFrequencyScore(n):
    s=str(n)
    freq={}
    for i in s:
        if int(i) in freq:
            freq[int(i)]+=1
        else:
            freq[int(i)]=1
    ans=0
    for k,v in freq.items():
        ans+=k*v
    return ans
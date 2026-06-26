# 1189. Maximum Number of Balloons


def maxNumberOfBalloons(text):
    freq={"b":0,"a":0,"l":0,"o":0,"n":0}
    a={"b","a","l","o","n"}
    for i in text:
        if i in a:
            freq[i]+=1
    mnfreq=float("inf")
    for k,v in freq.items():
        if k in {"b","a","n"} :
            mnfreq=min(mnfreq,v)
        else:
            mnfreq=min(mnfreq,v//2)
    return mnfreq
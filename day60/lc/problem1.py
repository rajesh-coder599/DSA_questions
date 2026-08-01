# 3016. Minimum Number of Pushes to Type Word II


def minimumPushes(word):
    from collections import defaultdict
    freq=defaultdict(int)
    for i in word:
        freq[i]+=1
    value=list(freq.values())
    value.sort(reverse=True)
    track=0
    ans=0
    for v in value:
        ans+=(track//8 +1)*v
        track+=1
    return ans
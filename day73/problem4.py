# 6. Zigzag Conversion



def convert(s,numRows):
    from collections import defaultdict
    rows=defaultdict(str)
    r=1
    direction=1
    for i in s:
        rows[r]+=i
        if r==numRows:
            direction=0
        if r==1:
            direction=1
        if direction==1:
            r+=1
        if direction==0:
            r-=1
    ans=""
    for v in rows.values():
        ans+=v
    return ans
# 2230B. Digit String

t=int(input())
for _ in range(t):
    s=input()
    four=s.count("4")
    total13=0
    for i in s:
        if i in ("1","3"):
            total13+=1
        
    rem13=total13
    tows=0
    ans=len(s)

    for i in range(len(s)+1):
        kept=tows+rem13
        ans=min(ans,len(s)-kept)

        if i==len(s):
            break

        if s[i]=="2" :
            tows+=1
        elif s[i] in "13" :
            rem13-=1

    print(ans)
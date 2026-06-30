# C. RemovevomeR



t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if s[0]==s[-1] :
        print(1)
        continue
    check=0
    for i in range(n-1):
        if s[i]!=s[i+1]:
            check+=1
    if check>1:
        print(1)
    else:
        print(2)
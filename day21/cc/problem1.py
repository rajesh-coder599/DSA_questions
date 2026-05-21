# HTML Tags

t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    if n<=3:
        print("Error")
        continue
    ok=True
    if s[:2]!="</" or s[-1]!=">" :
        print("Error")
        continue
    for i in range(2,n-1):
        a=s[i]
        if not (a.isdigit() or (a.isalpha() and a.islower())) :
            ok=False
            break
    if ok:
        print("Success")
    else:
        print("Error")
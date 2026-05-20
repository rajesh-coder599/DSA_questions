# HTML Tags

t=int(input())
for _ in range(t):
    s=input()
    check={"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
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
        if a not in check :
            print("Error")
            print("fuck")
            ok=False
            break
    if ok:
        print("Success")
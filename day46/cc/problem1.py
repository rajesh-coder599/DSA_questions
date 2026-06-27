# Harrenhal


t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    i=0
    j=n-1
    check=True
    while i<=j:
        if s[i] != s[j] :
            check=False
            break
        i+=1
        j-=1
    if check:
        print(1)
    else:
        print(2)